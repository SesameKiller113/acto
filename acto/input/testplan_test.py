import unittest
from unittest.mock import MagicMock
from acto.input.testplan import InputTreeNode, TestPlan, TestGroup, TestCase

class TestInputTreeNode(unittest.TestCase):

    def test_add_child(self):
        parent = InputTreeNode(['parent'])
        child = InputTreeNode(['child'])
        parent.add_child('child', child)
        self.assertEqual(parent.children['child'], child)
        self.assertEqual(child.parent, parent)

    def test_set_used(self):
        parent = InputTreeNode(['parent'])
        node = InputTreeNode(['node'])
        parent.add_child('node', node)
        node.set_used()
        self.assertTrue(node.used)
        self.assertTrue(parent.used)  # Testing if parents are also marked as used

    def test_add_testcases_by_path(self):
        root = InputTreeNode(['root'])
        child = InputTreeNode(['child'])
        subchild = InputTreeNode(['subchild'])
        root.add_child('child', child)
        child.add_child('subchild', subchild)
        testcase1 = MagicMock(spec=TestCase)
        testcase2 = MagicMock(spec=TestCase)
        root.add_testcases_by_path([testcase1, testcase2], ['child', 'subchild'])
        self.assertEqual(len(root.children['child'].children['subchild'].testcases), 2)

    def test_disable_subtree(self):
        root = InputTreeNode(['root'])
        child1 = InputTreeNode(['child1'])
        child2 = InputTreeNode(['child2'])
        root.add_child('child1', child1)
        root.add_child('child2', child2)
        root.disable_subtree()
        self.assertTrue(root.subtree_disabled)


class TestTestPlan(unittest.TestCase):

    def test_select_fields(self):
        root = InputTreeNode(['root'])
        # Add testcases and children to root
        testcase = MagicMock(spec=TestCase)
        root.add_testcases([testcase])
        testplan = TestPlan(root)
        selected_fields = testplan.select_fields(5)
        self.assertEqual(len(selected_fields), 1)  # Assuming only one eligible field is added

    def test_add_testcases_by_path(self):
        root = InputTreeNode(['root'])
        child = InputTreeNode(['child'])
        subchild = InputTreeNode(['subchild'])
        root.add_child('child', child)
        child.add_child('subchild', subchild)
        testcase1 = MagicMock(spec=TestCase)
        testcase2 = MagicMock(spec=TestCase)
        testplan = TestPlan(root)
        testplan.add_testcases_by_path([testcase1, testcase2], ['child', 'subchild'])
        self.assertEqual(len(root.children['child'].children['subchild'].testcases), 2)


class TestTestGroup(unittest.TestCase):

    def test_discard_testcase(self):
        testcase = MagicMock(spec=TestCase)
        group = TestGroup([(['path'], testcase)])
        discarded_testcases = {}
        group.discard_testcase(discarded_testcases)
        self.assertTrue(('["path"]' in discarded_testcases) and (testcase in discarded_testcases['["path"]']))

if __name__ == '__main__':
    unittest.main()

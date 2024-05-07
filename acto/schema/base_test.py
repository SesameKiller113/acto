import unittest
from unittest.mock import MagicMock
from acto.schema.anyof import TreeNode, BaseSchema
from acto.input.property_attribute import PropertyAttribute

class TestTreeNode(unittest.TestCase):
    def setUp(self):
        self.path = ["test_path"]
        self.tree_node = TreeNode(self.path)

    def test_init(self):
        self.assertEqual(self.tree_node.path, self.path)
        self.assertIsNone(self.tree_node.parent)
        self.assertDictEqual(self.tree_node.children, {})

    def test_add_child(self):
        child_node = TreeNode(["child_path"])
        self.tree_node.add_child("child_key", child_node)
        self.assertIn("child_key", self.tree_node.children)
        self.assertEqual(self.tree_node.children["child_key"], child_node)
        self.assertEqual(child_node.parent, self.tree_node)
        self.assertEqual(child_node.path, ["test_path", "child_key"])

    def test_set_parent(self):
        parent_node = TreeNode(["parent_path"])
        self.tree_node.set_parent(parent_node)
        self.assertEqual(self.tree_node.parent, parent_node)

    def test_get_node_by_path(self):
        child_node = TreeNode(["child_path"])
        self.tree_node.add_child("child_key", child_node)
        self.assertEqual(self.tree_node.get_node_by_path(["child_key"]), child_node)

    def test_get_children(self):
        self.assertDictEqual(self.tree_node.get_children(), {})

    def test_get_path(self):
        self.assertEqual(self.tree_node.get_path(), self.path)

    def test_traverse_func(self):
        func = MagicMock()
        self.tree_node.traverse_func(func)
        func.assert_called_with(self.tree_node)

    def test_getitem(self):
        child_node = TreeNode(["child_path"])
        self.tree_node.add_child("child_key", child_node)
        self.assertEqual(self.tree_node["child_key"], child_node)

    def test_contains(self):
        child_node = TreeNode(["child_path"])
        self.tree_node.add_child("child_key", child_node)
        self.assertTrue("child_key" in self.tree_node)

    def test_str(self):
        self.assertEqual(str(self.tree_node), "['test_path']")

    def test_deepcopy(self):
        child_node = TreeNode(["child_path"])
        self.tree_node.add_child("child_key", child_node)
        copied_node = self.tree_node.deepcopy(["copied_path"])
        self.assertEqual(copied_node.path, ["copied_path"])
        self.assertEqual(copied_node.children["child_key"].path, ["copied_path", "child_key"])

class TestBaseSchema(unittest.TestCase):
    def setUp(self):
        self.path = ["test_path"]
        self.schema = {"default": "default_value", "enum": ["value1", "value2"]}
        self.base_schema = BaseSchema(self.path, self.schema)

    def test_init(self):
        self.assertEqual(self.base_schema.path, self.path)
        self.assertEqual(self.base_schema.raw_schema, self.schema)
        self.assertEqual(self.base_schema.default, "default_value")
        self.assertEqual(self.base_schema.enum, ["value1", "value2"])
        self.assertEqual(self.base_schema.examples, [])
        self.assertIsInstance(self.base_schema.attributes, PropertyAttribute)
        self.assertFalse(self.base_schema.copied_over)
        self.assertFalse(self.base_schema.over_specified)
        self.assertFalse(self.base_schema.problematic)
        self.assertFalse(self.base_schema.patch)
        self.assertFalse(self.base_schema.mapped)
        self.assertEqual(self.base_schema.used_fields, [])

    def test_get_path(self):
        self.assertEqual(self.base_schema.get_path(), self.path)

    def test_validate(self):
        self.assertTrue(self.base_schema.validate("value1"))
        self.assertFalse(self.base_schema.validate("invalid_value"))

    def test_gen(self):
        with self.assertRaises(NotImplementedError):
            self.base_schema.gen()

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import MagicMock
from acto.schema.boolean import BooleanSchema 

class TestBooleanSchema(unittest.TestCase):
    def test_init(self):
        path = ["test", "path"]
        schema = {
            "type": "boolean",
            "default": True
        }
        boolean_schema = BooleanSchema(path, schema)

        self.assertEqual(boolean_schema.path, path)
        self.assertEqual(boolean_schema.default, True)

    def test_get_all_schemas(self):
        path = ["test", "path"]
        schema = {
            "type": "boolean"
        }
        boolean_schema = BooleanSchema(path, schema)

        all_schemas = boolean_schema.get_all_schemas()

        self.assertEqual(all_schemas, ([boolean_schema], [], []))

    def test_get_normal_semantic_schemas(self):
        path = ["test", "path"]
        schema = {
            "type": "boolean"
        }
        boolean_schema = BooleanSchema(path, schema)

        normal_schemas, semantic_schemas = boolean_schema.get_normal_semantic_schemas()

        self.assertEqual(normal_schemas, [boolean_schema])
        self.assertEqual(semantic_schemas, [])

    def test_to_tree(self):
        path = ["test", "path"]
        schema = {
            "type": "boolean"
        }
        boolean_schema = BooleanSchema(path, schema)

        tree_node = boolean_schema.to_tree()

        self.assertEqual(tree_node.path, path)

    def test_load_examples(self):
        path = ["test", "path"]
        schema = {
            "type": "boolean"
        }
        boolean_schema = BooleanSchema(path, schema)

        boolean_schema.load_examples(True)
        # Should not raise any exception

    def test_set_default(self):
        path = ["test", "path"]
        schema = {
            "type": "boolean"
        }
        boolean_schema = BooleanSchema(path, schema)

        boolean_schema.set_default(True)

        self.assertEqual(boolean_schema.default, True)

    def test_empty_value(self):
        path = ["test", "path"]
        schema = {
            "type": "boolean"
        }
        boolean_schema = BooleanSchema(path, schema)

        empty_value = boolean_schema.empty_value()

        self.assertEqual(empty_value, False)

    def test_gen(self):
        path = ["test", "path"]
        schema = {
            "type": "boolean"
        }
        boolean_schema = BooleanSchema(path, schema)

        generated = boolean_schema.gen()

        self.assertIsInstance(generated, bool)

if __name__ == '__main__':
    unittest.main()

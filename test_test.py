import unittest
from unittest.mock import MagicMock
from acto.schema.integer import IntegerSchema 

class TestIntegerSchema(unittest.TestCase):
    def test_init(self):
        path = ["test", "path"]
        schema = {
            "type": "integer",
            "default": 42
        }
        integer_schema = IntegerSchema(path, schema)

        self.assertEqual(integer_schema.path, path)
        self.assertEqual(integer_schema.default, 42)

    def test_get_all_schemas(self):
        path = ["test", "path"]
        schema = {
            "type": "integer"
        }
        integer_schema = IntegerSchema(path, schema)

        all_schemas = integer_schema.get_all_schemas()

        self.assertEqual(all_schemas, ([integer_schema], [], []))

    def test_get_normal_semantic_schemas(self):
        path = ["test", "path"]
        schema = {
            "type": "integer"
        }
        integer_schema = IntegerSchema(path, schema)

        normal_schemas, semantic_schemas = integer_schema.get_normal_semantic_schemas()

        self.assertEqual(normal_schemas, [integer_schema])
        self.assertEqual(semantic_schemas, [])

    def test_to_tree(self):
        path = ["test", "path"]
        schema = {
            "type": "integer"
        }
        integer_schema = IntegerSchema(path, schema)

        tree_node = integer_schema.to_tree()

        self.assertEqual(tree_node.path, path)

    def test_load_examples(self):
        path = ["test", "path"]
        schema = {
            "type": "integer"
        }
        integer_schema = IntegerSchema(path, schema)

        integer_schema.load_examples(10)
        # Should not raise any exception

    def test_set_default(self):
        path = ["test", "path"]
        schema = {
            "type": "integer"
        }
        integer_schema = IntegerSchema(path, schema)

        integer_schema.set_default(42)

        self.assertEqual(integer_schema.default, 42)

    def test_empty_value(self):
        path = ["test", "path"]
        schema = {
            "type": "integer"
        }
        integer_schema = IntegerSchema(path, schema)

        empty_value = integer_schema.empty_value()

        self.assertEqual(empty_value, 0)

    def test_gen(self):
        path = ["test", "path"]
        schema = {
            "type": "integer",
            "minimum": 1,
            "maximum": 10
        }
        integer_schema = IntegerSchema(path, schema)

        generated = integer_schema.gen()

        self.assertIsInstance(generated, int)

if __name__ == '__main__':
    unittest.main()

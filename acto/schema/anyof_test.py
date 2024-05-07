import unittest
from unittest.mock import MagicMock
from acto.schema.anyof import AnyOfSchema

class TestAnyOfSchema(unittest.TestCase):
    def setUp(self):
        # Create an example schema and path
        self.schema = {
            "anyOf": [
                {"type": "integer", "minimum": 1, "maximum": 10},
                {"type": "string", "minLength": 3, "maxLength": 5}
            ]
        }
        self.path = ["root", "any_of"]

    def test_init(self):
        # Test initialization
        any_of_schema = AnyOfSchema(self.path, self.schema)
        self.assertEqual(any_of_schema.path, self.path)
        self.assertIsInstance(any_of_schema.possibilities, list)
        self.assertEqual(len(any_of_schema.possibilities), 2)

    def test_get_possibilities(self):
        # Test getting all possibilities of the anyOf schema
        any_of_schema = AnyOfSchema(self.path, self.schema)
        possibilities = any_of_schema.get_possibilities()
        self.assertIsInstance(possibilities, list)
        self.assertEqual(len(possibilities), 2)

    def test_get_all_schemas(self):
        # Test getting all schemas
        any_of_schema = AnyOfSchema(self.path, self.schema)
        schemas_tuple = any_of_schema.get_all_schemas()
        self.assertIsInstance(schemas_tuple, tuple)
        self.assertEqual(len(schemas_tuple[0]), 1)
        self.assertEqual(len(schemas_tuple[1]), 0)
        self.assertEqual(len(schemas_tuple[2]), 0)

    def test_get_normal_semantic_schemas(self):
        # Test getting normal and semantic schemas
        any_of_schema = AnyOfSchema(self.path, self.schema)
        normal_schemas, semantic_schemas = any_of_schema.get_normal_semantic_schemas()
        self.assertIsInstance(normal_schemas, list)
        self.assertIsInstance(semantic_schemas, list)
        self.assertEqual(len(normal_schemas), 3)
        self.assertEqual(len(semantic_schemas), 0)

    def test_empty_value(self):
        # Test empty value
        any_of_schema = AnyOfSchema(self.path, self.schema)
        empty_value = any_of_schema.empty_value()
        self.assertIsNone(empty_value)

    def test_to_tree(self):
        # Test generating tree structure
        any_of_schema = AnyOfSchema(self.path, self.schema)
        tree_node = any_of_schema.to_tree()
        self.assertEqual(tree_node.path, self.path)

    def test_load_examples(self):
        # Test loading examples
        any_of_schema = AnyOfSchema(self.path, self.schema)
        example = 5  
        any_of_schema.load_examples(example)
        self.assertEqual(len(any_of_schema.possibilities[0].examples), 1)

    def test_set_default(self):
        # Test setting default value
        any_of_schema = AnyOfSchema(self.path, self.schema)
        instance = MagicMock()
        instance = 6 
        any_of_schema.set_default(instance)
        self.assertEqual(any_of_schema.default, 6)

    def test_gen(self):
        # Test generating random value
        any_of_schema = AnyOfSchema(self.path, self.schema)
        generated_value = any_of_schema.gen()
        self.assertTrue(isinstance(generated_value, (int, str)))

    def test_str(self):
        # Test string representation
        any_of_schema = AnyOfSchema(self.path, self.schema)
        string_repr = str(any_of_schema)
        self.assertTrue(string_repr[0] == '[')
        self.assertTrue(string_repr[len(string_repr)-1] == ']')

if __name__ == '__main__':
    unittest.main()
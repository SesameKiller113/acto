import unittest
from unittest.mock import MagicMock
from acto.schema.object import ObjectSchema 

class TestObjectSchema(unittest.TestCase):
    def test_get_all_schemas(self):
        path = ["test", "path"]
        schema = {
            "type": "object",
            "properties": {
                "prop1": {"type": "string"},
                "prop2": {"type": "integer"}
            }
        }
        object_schema = ObjectSchema(path, schema)

        # Mock extract_schema to return a boolean instead of a dictionary
        object_schema.extract_schema = MagicMock(return_value=True)

        all_schemas = object_schema.get_all_schemas()

        self.assertEqual(len(all_schemas[0]), 3)
        self.assertEqual(len(all_schemas[1]), 0)
        self.assertEqual(len(all_schemas[2]), 0)

    def test_get_normal_semantic_schemas(self):
        path = ["test", "path"]
        schema = {
            "type": "object",
            "properties": {
                "prop1": {"type": "string"},
                "prop2": {"type": "integer"}
            }
        }
        object_schema = ObjectSchema(path, schema)

        # Mock extract_schema to return a boolean instead of a dictionary
        object_schema.extract_schema = MagicMock(return_value=True)

        normal_schemas, semantic_schemas = object_schema.get_normal_semantic_schemas()

        self.assertEqual(len(normal_schemas), 3)
        self.assertEqual(len(semantic_schemas), 0)

if __name__ == '__main__':
    unittest.main()

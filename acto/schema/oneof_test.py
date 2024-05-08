import unittest
from unittest.mock import MagicMock
from acto.schema.oneof import OneOfSchema 

class TestOneOfSchema(unittest.TestCase):
    def test_get_all_schemas(self):
        path = ["test", "path"]
        schema = {
            "oneOf": [
                {"type": "string"},
                {"type": "integer"}
            ]
        }
        oneof_schema = OneOfSchema(path, schema)

        all_schemas = oneof_schema.get_all_schemas()

        self.assertEqual(len(all_schemas[0]), 1)
        self.assertEqual(len(all_schemas[1]), 0)
        self.assertEqual(len(all_schemas[2]), 0)

    def test_get_normal_semantic_schemas(self):
        path = ["test", "path"]
        schema = {
            "oneOf": [
                {"type": "string"},
                {"type": "integer"}
            ]
        }
        oneof_schema = OneOfSchema(path, schema)

        normal_schemas, semantic_schemas = oneof_schema.get_normal_semantic_schemas()

        self.assertEqual(len(normal_schemas), 3)
        self.assertEqual(len(semantic_schemas), 0)

if __name__ == '__main__':
    unittest.main()

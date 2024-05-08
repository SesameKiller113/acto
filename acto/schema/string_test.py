import unittest
from unittest.mock import MagicMock
from acto.schema.string import StringSchema


class TestStringSchema(unittest.TestCase):
    def test_init(self):
        path = ["test", "path"]
        schema = {
            "type": "string",
            "minLength": 5,
            "maxLength": 10,
            "pattern": r"^\d{5}$"
        }
        string_schema = StringSchema(path, schema)

        self.assertEqual(string_schema.path, path)
        self.assertEqual(string_schema.min_length, 5)
        self.assertEqual(string_schema.max_length, 10)
        self.assertEqual(string_schema.pattern, r"^\d{5}$")

    def test_get_all_schemas(self):
        path = ["test", "path"]
        schema = {"type": "string"}
        string_schema = StringSchema(path, schema)

        all_schemas = string_schema.get_all_schemas()

        self.assertEqual(len(all_schemas[0]), 1)
        self.assertEqual(len(all_schemas[1]), 0)
        self.assertEqual(len(all_schemas[2]), 0)

    def test_get_normal_semantic_schemas(self):
        path = ["test", "path"]
        schema = {"type": "string"}
        string_schema = StringSchema(path, schema)

        normal_schemas, semantic_schemas = string_schema.get_normal_semantic_schemas()

        self.assertEqual(len(normal_schemas), 1)
        self.assertEqual(len(semantic_schemas), 0)

    # Add more test cases as needed...

if __name__ == '__main__':
    unittest.main()

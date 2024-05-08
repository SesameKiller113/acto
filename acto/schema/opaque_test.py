import unittest
from acto.schema.opaque import OpaqueSchema 

class TestOpaqueSchema(unittest.TestCase):
    def test_get_all_schemas(self):
        opaque_schema = OpaqueSchema(["test", "path"], {})

        all_schemas = opaque_schema.get_all_schemas()

        self.assertEqual(len(all_schemas[0]), 0)
        self.assertEqual(len(all_schemas[1]), 0)
        self.assertEqual(len(all_schemas[2]), 0)

    def test_get_normal_semantic_schemas(self):
        opaque_schema = OpaqueSchema(["test", "path"], {})

        normal_schemas, semantic_schemas = opaque_schema.get_normal_semantic_schemas()

        self.assertEqual(len(normal_schemas), 0)
        self.assertEqual(len(semantic_schemas), 0)

if __name__ == '__main__':
    unittest.main()

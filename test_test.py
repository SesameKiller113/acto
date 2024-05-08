import unittest
from unittest.mock import MagicMock, patch

from acto.input.known_schemas.known_schema import (
    ResourceRequirementsSchema,
    StorageResourceRequirementsSchema,
    ComputeResourceRequirementsSchema,
)


class TestResourceRequirementsSchema(unittest.TestCase):

    def test_resource_requirements_schema_match(self):
        schema = ResourceRequirementsSchema(None)
        self.assertTrue(ResourceRequirementsSchema.Match(schema))

    def test_compute_resource_requirements_schema_match(self):
        schema = ComputeResourceRequirementsSchema(None)
        self.assertTrue(ComputeResourceRequirementsSchema.Match(schema))

    def test_storage_resource_requirements_schema_match(self):
        schema = StorageResourceRequirementsSchema(None)
        self.assertTrue(StorageResourceRequirementsSchema.Match(schema))

    def test_compute_resource_requirements_schema_gen(self):
        schema = ComputeResourceRequirementsSchema(None)
        result = schema.gen()
        expected_result = {
            "requests": {
                "cpu": "800m",
                "memory": "1000m"
            },
            "limits": {
                "cpu": "800m",
                "memory": "1000m"
            }
        }
        self.assertEqual(result, expected_result)

    def test_storage_resource_requirements_schema_gen(self):
        schema = StorageResourceRequirementsSchema(None)
        result = schema.gen()
        expected_result = {
            "requests": {
                "storage": "1000m"
            },
        }
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()

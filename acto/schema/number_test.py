import unittest
from unittest.mock import MagicMock
from acto.schema.number import NumberSchema

class TestNumberSchema(unittest.TestCase):

    def setUp(self):
        # Create an example schema and path
        self.schema = {
            "minimum": 1,
            "maximum": 10,
            "exclusiveMinimum": True,
            "multipleOf": 2
        }
        self.path = ["root", "number"]

    def test_init(self):
        # Test initialization
        number_schema = NumberSchema(self.path, self.schema)
        self.assertEqual(number_schema.path, self.path)
        self.assertEqual(number_schema.minimum, self.schema["minimum"])
        self.assertEqual(number_schema.maximum, self.schema["maximum"])
        self.assertTrue(number_schema.exclusive_minimum)
        self.assertEqual(number_schema.multiple_of, self.schema["multipleOf"])

    def test_get_all_schemas(self):
        # Test get_all_schemas method
        number_schema = NumberSchema(self.path, self.schema)
        number_schema.problematic = False
        self.assertEqual(number_schema.get_all_schemas(), ([number_schema], [], []))

    def test_get_normal_semantic_schemas(self):
        # Test get_normal_semantic_schemas method
        number_schema = NumberSchema(self.path, self.schema)
        number_schema.problematic = False
        self.assertEqual(number_schema.get_normal_semantic_schemas(), ([number_schema], []))

    def test_to_tree(self):
        # Test to_tree method
        number_schema = NumberSchema(self.path, self.schema)
        tree_node = number_schema.to_tree()
        self.assertEqual(tree_node.path, self.path)

    def test_load_examples(self):
        # Test load_examples method
        number_schema = NumberSchema(self.path, self.schema)
        number_schema.examples = []
        example_value = 3.5
        number_schema.load_examples(example_value)
        self.assertEqual(number_schema.examples, [example_value])

    def test_set_default(self):
        # Test set_default method
        number_schema = NumberSchema(self.path, self.schema)
        instance = MagicMock()
        instance.__float__.return_value = 7.2
        number_schema.set_default(instance)
        self.assertEqual(number_schema.default, 7.2)

    def test_empty_value(self):
        # Test empty_value method
        number_schema = NumberSchema(self.path, self.schema)
        self.assertEqual(number_schema.empty_value(), 0)

    def test_gen(self):
        # Test gen method
        number_schema = NumberSchema(self.path, self.schema)
        generated_value = number_schema.gen()
        self.assertTrue(number_schema.minimum <= generated_value <= number_schema.maximum)

    def test_str(self):
        # Test __str__ method
        number_schema = NumberSchema(self.path, self.schema)
        self.assertEqual(str(number_schema), "Number")

if __name__ == '__main__':
    unittest.main()
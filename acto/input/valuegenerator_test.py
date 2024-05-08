import unittest
from unittest.mock import MagicMock
from acto.schema import StringSchema
from acto.input.valuegenerator import (
    StringGenerator, NumberGenerator, IntegerGenerator, 
    OpaqueGenerator, ObjectGenerator, ArrayGenerator,
    AnyOfGenerator, OneOfGenerator,BooleanGenerator)

class TestStringGenerator(unittest.TestCase):
    
    def setUp(self):
        self.path = ['root', 'child', 'subchild']
        self.schema = {
            'type': 'string',
            'maxLength': 10,
            'minLength': 3,
            'pattern': r'[a-zA-Z]+'
        }
        self.string_generator = StringGenerator(self.path, self.schema)

    def test_gen(self):
        generated_string = self.string_generator.gen()
        self.assertTrue(isinstance(generated_string, str))
        self.assertRegex(generated_string, r'[a-zA-Z]+')

    def test_num_cases(self):
        self.assertEqual(self.string_generator.num_cases(), 3)

    def test_num_fields(self):
        self.assertEqual(self.string_generator.num_fields(), 1)

    def test_to_tree(self):
        input_tree_node = self.string_generator.to_tree()
        self.assertEqual(input_tree_node.path, self.path)

class TestNumberGenerator(unittest.TestCase):
    
    def setUp(self):
        self.path = ['root', 'child', 'subchild']
        self.schema = {
            'type': 'number',
            'minimum': 0,
            'maximum': 10,
            'multipleOf': 2
        }
        self.number_generator = NumberGenerator(self.path, self.schema)

    def test_gen(self):
        generated_number = self.number_generator.gen()
        self.assertTrue(isinstance(generated_number, float))
        self.assertTrue(generated_number >= 0 and generated_number <= 10)

    def test_num_cases(self):
        self.assertEqual(self.number_generator.num_cases(), 3)

    def test_num_fields(self):
        self.assertEqual(self.number_generator.num_fields(), 1)

    def test_to_tree(self):
        input_tree_node = self.number_generator.to_tree()
        self.assertEqual(input_tree_node.path, self.path)

class TestIntegerGenerator(unittest.TestCase):
    
    def setUp(self):
        self.path = ['root', 'child', 'subchild']
        self.schema = {
            'type': 'integer',
            'minimum': 0,
            'maximum': 10,
            'multipleOf': 2
        }
        self.integer_generator = IntegerGenerator(self.path, self.schema)

    def test_gen(self):
        generated_integer = self.integer_generator.gen()
        self.assertTrue(isinstance(generated_integer, int))
        self.assertTrue(generated_integer >= 0 and generated_integer <= 10)
        self.assertEqual(generated_integer % 2, 0)

    def test_num_cases(self):
        self.assertEqual(self.integer_generator.num_cases(), 3)

    def test_num_fields(self):
        self.assertEqual(self.integer_generator.num_fields(), 1)

    def test_to_tree(self):
        input_tree_node = self.integer_generator.to_tree()
        self.assertEqual(input_tree_node.path, self.path)

class TestObjectGenerator(unittest.TestCase):
    
    def setUp(self):
        self.path = ['root', 'child', 'subchild']
        self.schema = {
            'type': 'object',
            'properties': {
                'prop1': {'type': 'string'},
                'prop2': {'type': 'integer'},
                'prop3': {'type': 'boolean'}
            },
            'additionalProperties': {'type': 'string'}
        }
        self.object_generator = ObjectGenerator(self.path, self.schema)

    def test_gen(self):
        generated_object = self.object_generator.gen()
        self.assertIsInstance(generated_object, dict)
        self.assertTrue(all(isinstance(key, str) for key in generated_object.keys()))
        self.assertTrue(all(isinstance(value, (str, int, bool)) or value is None for value in generated_object.values()))

    def test_to_tree(self):
        input_tree_node = self.object_generator.to_tree()
        self.assertEqual(input_tree_node.path, self.path)
        self.assertEqual(len(input_tree_node.children), 4)  # Number of properties and additional properties

class TestArrayGenerator(unittest.TestCase):
    
    def setUp(self):
        self.path = ['root', 'child', 'subchild']
        self.schema = {
            'type': 'array',
            'items': {'type': 'integer'},
            'minItems': 3,
            'maxItems': 5
        }
        self.array_generator = ArrayGenerator(self.path, self.schema)

    def test_gen(self):
        generated_array = self.array_generator.gen()
        self.assertIsInstance(generated_array, list)
        self.assertTrue(len(generated_array) >= 3 and len(generated_array) <= 5)
        self.assertTrue(all(isinstance(item, int) for item in generated_array))

    def test_num_fields(self):
        self.assertEqual(self.array_generator.num_fields(), 2)  # Two fields including item schema

    def test_to_tree(self):
        input_tree_node = self.array_generator.to_tree()
        self.assertEqual(input_tree_node.path, self.path)
        self.assertEqual(len(input_tree_node.children), 1)  # Only one child for item schema

class TestAnyOfGenerator(unittest.TestCase):
    
    def setUp(self):
        self.path = ['root', 'child', 'subchild']
        self.schema = {
            'anyOf': [
                {'type': 'string'},
                {'type': 'number'}
            ]
        }
        self.any_of_generator = AnyOfGenerator(self.path, self.schema)

    def test_gen(self):
        generated_value = self.any_of_generator.gen()
        self.assertTrue(isinstance(generated_value, (str, int, float)))

    def test_num_cases(self):
        self.assertGreaterEqual(self.any_of_generator.num_cases(), 2)  # At least two cases from possibilities

    def test_num_fields(self):
        self.assertGreaterEqual(self.any_of_generator.num_fields(), 1)  # At least one field from possibilities

    def test_to_tree(self):
        input_tree_node = self.any_of_generator.to_tree()
        self.assertEqual(input_tree_node.path, self.path)

class TestOneOfGenerator(unittest.TestCase):
    
    def setUp(self):
        self.path = ['root', 'child', 'subchild']
        self.schema = {
            'oneOf': [
                {'type': 'string'},
                {'type': 'number'}
            ]
        }
        self.one_of_generator = OneOfGenerator(self.path, self.schema)

    def test_gen(self):
        generated_value = self.one_of_generator.gen()
        self.assertTrue(isinstance(generated_value, (str, int, float)))

    def test_to_tree(self):
        input_tree_node = self.one_of_generator.to_tree()
        self.assertEqual(input_tree_node.path, self.path)

class TestBooleanGenerator(unittest.TestCase):
    
    def setUp(self):
        self.path = ['root', 'child', 'subchild']
        self.schema = {
            'type': 'boolean',
            'default': False
        }
        self.boolean_generator = BooleanGenerator(self.path, self.schema)

    def test_gen(self):
        generated_boolean = self.boolean_generator.gen()
        self.assertTrue(isinstance(generated_boolean, bool))

    def test_num_cases(self):
        self.assertEqual(self.boolean_generator.num_cases(), 3)

    def test_num_fields(self):
        self.assertEqual(self.boolean_generator.num_fields(), 1)

    def test_to_tree(self):
        input_tree_node = self.boolean_generator.to_tree()
        self.assertEqual(input_tree_node.path, self.path)

    def test_toggle_on_precondition(self):
        self.assertTrue(self.boolean_generator.toggle_on_precondition(False))
        self.assertFalse(self.boolean_generator.toggle_on_precondition(True))

    def test_toggle_on(self):
        self.assertTrue(self.boolean_generator.toggle_on(False))
        self.assertTrue(self.boolean_generator.toggle_on(True))

    def test_toggle_off_precondition(self):
        self.assertTrue(self.boolean_generator.toggle_off_precondition(True))
        self.assertFalse(self.boolean_generator.toggle_off_precondition(False))

    def test_toggle_off(self):
        self.assertFalse(self.boolean_generator.toggle_off(True))
        self.assertFalse(self.boolean_generator.toggle_off(False))

    def test_delete_setup(self):
        self.assertTrue(self.boolean_generator.delete_setup(False))

class TestOpaqueGenerator(unittest.TestCase):
    
    def setUp(self):
        self.path = ['root', 'child', 'subchild']
        self.schema = {
            'type': 'opaque'
        }
        self.opaque_generator = OpaqueGenerator(self.path, self.schema)

    def test_gen(self):
        generated_value = self.opaque_generator.gen()
        self.assertIsNone(generated_value)

    def test_test_cases(self):
        test_cases, _ = self.opaque_generator.test_cases()
        self.assertEqual(len(test_cases), 0)  # No test cases

    def test_num_cases(self):
        self.assertEqual(self.opaque_generator.num_cases(), 1)  # Only one case, which is None

    def test_num_fields(self):
        self.assertEqual(self.opaque_generator.num_fields(), 1)

    def test_to_tree(self):
        input_tree_node = self.opaque_generator.to_tree()
        self.assertEqual(input_tree_node.path, self.path)

if __name__ == '__main__':
    unittest.main()

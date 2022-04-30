import unittest

from packer.ipacker import IPacker
from packer.packer_main import PackerType, Packer
from tests.objects_to_test import *


class PackerTester(unittest.TestCase):
    json_packer: IPacker = Packer.create_serializer(PackerType.JSON)
    yaml_packer: IPacker = Packer.create_serializer(PackerType.YAML)
    toml_packer: IPacker = Packer.create_serializer(PackerType.TOML)

    output_file_json: str = 'test_output.json'
    output_file_yaml: str = 'test_output.yaml'
    output_file_toml: str = 'test_output.toml'

    def test_int(self):
        for number in TEST_INTS:
            self.assertEqual(number, self.json_packer.loads(self.json_packer.dumps(number)))
            self.json_packer.dump(number, self.output_file_json)
            self.assertEqual(number, self.json_packer.load(self.output_file_json))

            self.assertEqual(number, self.yaml_packer.loads(self.yaml_packer.dumps(number)))
            self.yaml_packer.dump(number, self.output_file_yaml)
            self.assertEqual(number, self.yaml_packer.load(self.output_file_yaml))

            self.assertEqual(number, self.toml_packer.loads(self.toml_packer.dumps(number)))
            self.toml_packer.dump(number, self.output_file_toml)
            self.assertEqual(number, self.toml_packer.load(self.output_file_toml))

    def test_float(self):
        for number in TEST_FLOATS:
            self.assertEqual(number, self.json_packer.loads(self.json_packer.dumps(number)))
            self.json_packer.dump(number, self.output_file_json)
            self.assertEqual(number, self.json_packer.load(self.output_file_json))

            self.assertEqual(number, self.yaml_packer.loads(self.yaml_packer.dumps(number)))
            self.yaml_packer.dump(number, self.output_file_yaml)
            self.assertEqual(number, self.yaml_packer.load(self.output_file_yaml))

            self.assertEqual(number, self.toml_packer.loads(self.toml_packer.dumps(number)))
            self.toml_packer.dump(number, self.output_file_toml)
            self.assertEqual(number, self.toml_packer.load(self.output_file_toml))

    def test_str(self):
        for string in TEST_STRINGS:
            self.assertEqual(string, self.json_packer.loads(self.json_packer.dumps(string)))
            self.json_packer.dump(string, self.output_file_json)
            self.assertEqual(string, self.json_packer.load(self.output_file_json))

            self.assertEqual(string, self.yaml_packer.loads(self.yaml_packer.dumps(string)))
            self.yaml_packer.dump(string, self.output_file_yaml)
            self.assertEqual(string, self.yaml_packer.load(self.output_file_yaml))

            self.assertEqual(string, self.toml_packer.loads(self.toml_packer.dumps(string)))
            self.toml_packer.dump(string, self.output_file_toml)
            self.assertEqual(string, self.toml_packer.load(self.output_file_toml))

    def test_bool(self):
        for boolean in TEST_BOOLEANS:
            self.assertEqual(boolean, self.json_packer.loads(self.json_packer.dumps(boolean)))
            self.json_packer.dump(boolean, self.output_file_json)
            self.assertEqual(boolean, self.json_packer.load(self.output_file_json))

            self.assertEqual(boolean, self.yaml_packer.loads(self.yaml_packer.dumps(boolean)))
            self.yaml_packer.dump(boolean, self.output_file_yaml)
            self.assertEqual(boolean, self.yaml_packer.load(self.output_file_yaml))

            self.assertEqual(boolean, self.toml_packer.loads(self.toml_packer.dumps(boolean)))
            self.toml_packer.dump(boolean, self.output_file_toml)
            self.assertEqual(boolean, self.toml_packer.load(self.output_file_toml))

    def test_none(self):
        self.assertEqual(None, self.json_packer.loads(self.json_packer.dumps(None)))
        self.json_packer.dump(None, self.output_file_json)
        self.assertEqual(None, self.json_packer.load(self.output_file_json))

        self.assertEqual(None, self.yaml_packer.loads(self.yaml_packer.dumps(None)))
        self.yaml_packer.dump(None, self.output_file_yaml)
        self.assertEqual(None, self.yaml_packer.load(self.output_file_yaml))

        self.assertEqual(None, self.toml_packer.loads(self.toml_packer.dumps(None)))
        self.toml_packer.dump(None, self.output_file_toml)
        self.assertEqual(None, self.toml_packer.load(self.output_file_toml))

    def test_list(self):
        for array in TEST_LISTS:
            self.assertEqual(array, self.json_packer.loads(self.json_packer.dumps(array)))
            self.json_packer.dump(array, self.output_file_json)
            self.assertEqual(array, self.json_packer.load(self.output_file_json))

            self.assertEqual(array, self.yaml_packer.loads(self.yaml_packer.dumps(array)))
            self.yaml_packer.dump(array, self.output_file_yaml)
            self.assertEqual(array, self.yaml_packer.load(self.output_file_yaml))

            self.assertEqual(array, self.toml_packer.loads(self.toml_packer.dumps(array)))
            self.toml_packer.dump(array, self.output_file_toml)
            self.assertEqual(array, self.toml_packer.load(self.output_file_toml))

    def test_tuple(self):
        for array in TEST_TUPLES:
            self.assertEqual(array, self.json_packer.loads(self.json_packer.dumps(array)))
            self.json_packer.dump(array, self.output_file_json)
            self.assertEqual(array, self.json_packer.load(self.output_file_json))

            self.assertEqual(array, self.yaml_packer.loads(self.yaml_packer.dumps(array)))
            self.yaml_packer.dump(array, self.output_file_yaml)
            self.assertEqual(array, self.yaml_packer.load(self.output_file_yaml))

            self.assertEqual(array, self.toml_packer.loads(self.toml_packer.dumps(array)))
            self.toml_packer.dump(array, self.output_file_toml)
            self.assertEqual(array, self.toml_packer.load(self.output_file_toml))

    def test_dictionary(self):
        for dictionary in TEST_DICTIONARIES:
            self.assertEqual(dictionary, self.json_packer.loads(self.json_packer.dumps(dictionary)))
            self.json_packer.dump(dictionary, self.output_file_json)
            self.assertEqual(dictionary, self.json_packer.load(self.output_file_json))

            self.assertEqual(dictionary, self.yaml_packer.loads(self.yaml_packer.dumps(dictionary)))
            self.yaml_packer.dump(dictionary, self.output_file_yaml)
            self.assertEqual(dictionary, self.yaml_packer.load(self.output_file_yaml))

            self.assertEqual(dictionary, self.toml_packer.loads(self.toml_packer.dumps(dictionary)))
            self.toml_packer.dump(dictionary, self.output_file_toml)
            self.assertEqual(dictionary, self.toml_packer.load(self.output_file_toml))

    def test_complex_dictionaries_and_lists(self):
        for obj in TEST_COMPLEX_STRUCTS:
            self.assertEqual(obj, self.json_packer.loads(self.json_packer.dumps(obj)))
            self.json_packer.dump(obj, self.output_file_json)
            self.assertEqual(obj, self.json_packer.load(self.output_file_json))

            self.assertEqual(obj, self.yaml_packer.loads(self.yaml_packer.dumps(obj)))
            self.yaml_packer.dump(obj, self.output_file_yaml)
            self.assertEqual(obj, self.yaml_packer.load(self.output_file_yaml))

    def test_bytes(self):
        for obj in TEST_BYTES:
            self.assertEqual(obj, self.json_packer.loads(self.json_packer.dumps(obj)))
            self.json_packer.dump(obj, self.output_file_json)
            self.assertEqual(obj, self.json_packer.load(self.output_file_json))

            self.assertEqual(obj, self.yaml_packer.loads(self.yaml_packer.dumps(obj)))
            self.yaml_packer.dump(obj, self.output_file_yaml)
            self.assertEqual(obj, self.yaml_packer.load(self.output_file_yaml))

            self.assertEqual(obj, self.toml_packer.loads(self.toml_packer.dumps(obj)))
            self.toml_packer.dump(obj, self.output_file_toml)
            self.assertEqual(obj, self.toml_packer.load(self.output_file_toml))

    def test_functions(self):
        self.assertEqual(
            SIMPLE_FUNCTION_1(2022, -2),
            self.json_packer.loads(self.json_packer.dumps(SIMPLE_FUNCTION_1))(2022, -2)
        )

        self.json_packer.dump(SIMPLE_FUNCTION_1, self.output_file_json)
        self.assertEqual(
            SIMPLE_FUNCTION_1(2022, -2),
            self.json_packer.load(self.output_file_json)(2022, -2)
        )

        self.assertEqual(
            SIMPLE_FUNCTION_2(2022, 2022),
            self.json_packer.loads(self.json_packer.dumps(SIMPLE_FUNCTION_2))(2022, 2022)
        )

        self.json_packer.dump(SIMPLE_FUNCTION_2, self.output_file_json)
        self.assertEqual(
            SIMPLE_FUNCTION_2(2022, -2),
            self.json_packer.load(self.output_file_json)(2022, -2)
        )

        self.assertEqual(
            MORE_COMPLEX_FUNCTION(2022),
            self.json_packer.loads(self.json_packer.dumps(MORE_COMPLEX_FUNCTION))(2022)
        )

        self.json_packer.dump(MORE_COMPLEX_FUNCTION, self.output_file_json)
        self.assertEqual(
            MORE_COMPLEX_FUNCTION(math.pi / 2),
            self.json_packer.load(self.output_file_json)(math.pi / 2)
        )

        self.assertEqual(
            MEGA_COMPLEX_FUNCTION([5, 4, 3, 2, 1]),
            self.json_packer.loads(self.json_packer.dumps(MEGA_COMPLEX_FUNCTION))([5, 4, 3, 2, 1])
        )

        self.json_packer.dump(MEGA_COMPLEX_FUNCTION, self.output_file_json)
        self.assertEqual(
            MEGA_COMPLEX_FUNCTION([2022, 2021, 2020, 2019, 0, -5]),
            self.json_packer.load(self.output_file_json)([2022, 2021, 2020, 2019, 0, -5])
        )

        self.assertEqual(
            SIMPLE_FUNCTION_1(2022, -2),
            self.yaml_packer.loads(self.yaml_packer.dumps(SIMPLE_FUNCTION_1))(2022, -2)
        )

    def test_classes(self):
        first_instance: Test = Test('John', 19)

        json: str = self.json_packer.dumps(Test)
        yaml: str = self.yaml_packer.dumps(Test)
        NewTestFromJSON = self.json_packer.loads(json)
        NewTestFromYAML = self.yaml_packer.loads(yaml)

        second_instance_json: NewTestFromJSON = NewTestFromJSON('John', 19)
        second_instance_yaml: NewTestFromYAML = NewTestFromJSON('John', 19)

        self.assertEqual(str(second_instance_json), str(first_instance))
        self.assertEqual(str(second_instance_yaml), str(first_instance))
        self.assertEqual(Test.static_var_example, NewTestFromJSON.static_var_example)

    def test_instances(self):
        first_instance: Test = Test('John', 19)

        second_instance = self.json_packer.loads(self.json_packer.dumps(first_instance))

        self.assertEqual(str(first_instance), str(second_instance))

        second_instance.change_age()

        self.assertNotEqual(str(first_instance), str(second_instance))

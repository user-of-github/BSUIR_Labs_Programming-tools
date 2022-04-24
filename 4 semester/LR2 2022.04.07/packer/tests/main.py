import math
import unittest

from library.ipacker import IPacker
from library.packer import Packer, PackerType
from tests.objects_to_test import *


class TestJsonPacker(unittest.TestCase):
    json_packer: IPacker = Packer.create_serializer(PackerType.JSON)
    output_file: str = 'test_output.json'

    def test_int(self):
        for number in TEST_INTS:
            self.assertEqual(number, self.json_packer.loads(self.json_packer.dumps(number)))
            self.json_packer.dump(number, self.output_file)
            self.assertEqual(number, self.json_packer.load(self.output_file))

    def test_float(self):
        for number in TEST_FLOATS:
            self.assertEqual(number, self.json_packer.loads(self.json_packer.dumps(number)))
            self.json_packer.dump(number, self.output_file)
            self.assertEqual(number, self.json_packer.load(self.output_file))

    def test_str(self):
        for string in TEST_STRINGS:
            self.assertEqual(string, self.json_packer.loads(self.json_packer.dumps(string)))
            self.json_packer.dump(string, self.output_file)
            self.assertEqual(string, self.json_packer.load(self.output_file))

    def test_bool(self):
        self.assertEqual(True, self.json_packer.loads(self.json_packer.dumps(True)))
        for boolean in TEST_BOOLEANS:
            self.assertEqual(boolean, self.json_packer.loads(self.json_packer.dumps(boolean)))
            self.json_packer.dump(boolean, self.output_file)
            self.assertEqual(boolean, self.json_packer.load(self.output_file))

    def test_none(self):
        self.assertEqual(None, self.json_packer.loads(self.json_packer.dumps(None)))
        self.json_packer.dump(None, self.output_file)
        self.assertEqual(None, self.json_packer.load(self.output_file))

    def test_list(self):
        for array in TEST_LISTS:
            self.assertEqual(array, self.json_packer.loads(self.json_packer.dumps(array)))
            self.json_packer.dump(array, self.output_file)
            self.assertEqual(array, self.json_packer.load(self.output_file))

    def test_tuple(self):
        for array in TEST_TUPLES:
            self.assertEqual(array, self.json_packer.loads(self.json_packer.dumps(array)))
            self.json_packer.dump(array, self.output_file)
            self.assertEqual(array, self.json_packer.load(self.output_file))

    def test_dictionary(self):
        for dictionary in TEST_DICTIONARIES:
            self.assertEqual(dictionary, self.json_packer.loads(self.json_packer.dumps(dictionary)))
            self.json_packer.dump(dictionary, self.output_file)
            self.assertEqual(dictionary, self.json_packer.load(self.output_file))

    def test_complex_dictionaries_and_lists(self):
        for obj in TEST_COMPLEX_STRUCTS:
            self.assertEqual(obj, self.json_packer.loads(self.json_packer.dumps(obj)))
            self.json_packer.dump(obj, self.output_file)
            self.assertEqual(obj, self.json_packer.load(self.output_file))

    def test_bytes(self):
        for obj in TEST_BYTES:
            self.assertEqual(obj, self.json_packer.loads(self.json_packer.dumps(obj)))
            self.json_packer.dump(obj, self.output_file)
            self.assertEqual(obj, self.json_packer.load(self.output_file))

    def test_functions(self):
        self.assertEqual(
            SIMPLE_FUNCTION_1(2022, -2),
            self.json_packer.loads(self.json_packer.dumps(SIMPLE_FUNCTION_1))(2022, -2)
        )

        self.json_packer.dump(SIMPLE_FUNCTION_1, self.output_file)
        self.assertEqual(
            SIMPLE_FUNCTION_1(2022, -2),
            self.json_packer.load(self.output_file)(2022, -2)
        )

        self.assertEqual(
            SIMPLE_FUNCTION_2(2022, 2022),
            self.json_packer.loads(self.json_packer.dumps(SIMPLE_FUNCTION_2))(2022, 2022)
        )

        self.json_packer.dump(SIMPLE_FUNCTION_2, self.output_file)
        self.assertEqual(
            SIMPLE_FUNCTION_2(2022, -2),
            self.json_packer.load(self.output_file)(2022, -2)
        )

        self.assertEqual(
            MORE_COMPLEX_FUNCTION(2022),
            self.json_packer.loads(self.json_packer.dumps(MORE_COMPLEX_FUNCTION))(2022)
        )

        self.json_packer.dump(MORE_COMPLEX_FUNCTION, self.output_file)
        self.assertEqual(
            MORE_COMPLEX_FUNCTION(math.pi / 2),
            self.json_packer.load(self.output_file)(math.pi / 2)
        )

        self.assertEqual(
            MEGA_COMPLEX_FUNCTION([5, 4, 3, 2, 1]),
            self.json_packer.loads(self.json_packer.dumps(MEGA_COMPLEX_FUNCTION))([5, 4, 3, 2, 1])
        )

        self.json_packer.dump(MEGA_COMPLEX_FUNCTION, self.output_file)
        self.assertEqual(
            MEGA_COMPLEX_FUNCTION([2022, 2021, 2020, 2019, 0, -5]),
            self.json_packer.load(self.output_file)([2022, 2021, 2020, 2019, 0, -5])
        )

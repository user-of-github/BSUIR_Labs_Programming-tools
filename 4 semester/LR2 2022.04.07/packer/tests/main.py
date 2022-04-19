import unittest

from library.packer import Packer, PackerType


class TestPackerWithNumbers(unittest.TestCase):
    def test_int(self):
        json_parser = Packer.create_serializer(PackerType.JSON)
        test_numbers: list[int] = [1, 2, 3, 4, 0, -1, 19999, -2022, 2022, 123456789]

        for number in test_numbers:
            self.assertEqual(number, json_parser.loads(json_parser.dumps(number)))


if __name__ == '__main__':
    unittest.main()
import math
import sys

TEST_INTS: list[int] = [1, 2, 3, 4, 0, -1, 19999, -2022, 2022, 123456789]

TEST_FLOATS: list[float] = [1.0005, -2.1234, 3.0258480, 2022.20222022, 6, 7, -8, 0, 0.000]

TEST_STRINGS: list[str] = ['', 'some string', 'string with spaces', '    ',
                           '   string with Lots spaces and numbers: 1424848   ', ""]

TEST_BOOLEANS: list[bool] = [True, False]

TEST_LISTS: list[list] = [[1, -2, 3], [], ['string test   ', 4, 5.0, False], [[5, 6], [], [True, False]]]

TEST_DICTIONARIES: list[dict] = [{}, {'a': 'b', 'c': 'd'}, {'a': 25.5, 'b': False, 'c': None, 'd': '  string  '},
                                 {'type': 'int', 'value': 5}]

TEST_TUPLES: list[tuple] = [(1, 2, 3), (True, '2022 test', 5), (), (5, 7, 5.2, False)]

TEST_BYTES: list[bytes] = [b'\x00\x00\x00\x00\x00']

TEST_COMPLEX_STRUCTS: list = [
    [{'a': 2022, 'b': 4, 'c': 20, 'd': False}, True, None, 2022.0001],
    {'field1': True, 'field2': [1, 2, 3, {'a': True}], 'field3': {'field3_1': '   2022.0420   ', 'field3_2': 19}},
    [[[5, 6], True], False, True, 2022, [{}, [], {'field': [1, 2, 3]}], None, {'key': None}],
    [('key with value', [1]), {'author': 'User2022', 'message': 'Hi there ! How are you ? Greetings from April, 2022'}]
]

GLOBAL_INT: int = 42


def SIMPLE_FUNCTION_1(a: int, b: int) -> int:
    return (a * b) + GLOBAL_INT


def SIMPLE_FUNCTION_2(a: int, b: int) -> int:
    return (a * b) + GLOBAL_INT


GLOBAL_INT_2: int = 1


def MORE_COMPLEX_FUNCTION(argument: float) -> (float, int):
    print(f'SINUS of {argument} = ', math.sin(argument))
    return math.sin(argument), sys.getsizeof(argument)


GLOBAL_STRING: str = 'Hello from user-of-github !!!'


def MEGA_COMPLEX_FUNCTION(array: list[int]) -> (list, int, int, str, (float, int)):
    sorted_response: list = sorted(array)

    sum_response: int = 0

    for item in sorted_response:
        sum_response += item

    return sorted_response, sum_response, sum(array), GLOBAL_STRING, MORE_COMPLEX_FUNCTION(42)


class Test:
    static_var_example = 42

    def __init__(self, name: str, age: int):
        self.__name = name
        self._age = age

    def foo(self):
        print('hello from foo !')
        print(f'Check if we can use globals from class: {GLOBAL_STRING}')
        self.some_funct()

    def change_age(self):
        self._age += 1

    def some_funct(self):
        print('Hello from some_funct !, ', self.__name)

    def __str__(self):
        return f'Person: name = {self.__name}, age: {self._age}'

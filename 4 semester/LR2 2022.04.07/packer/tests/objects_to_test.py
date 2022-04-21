TEST_INTS: list[int] = [1, 2, 3, 4, 0, -1, 19999, -2022, 2022, 123456789]

TEST_FLOATS: list[float] = [1.0005, -2.1234, 3.0258480, 2022.20222022, 6, 7, -8, 0, 0.000]

TEST_STRINGS: list[str] = ['', 'some string', 'string with spaces', '    ',
                           '   string with Lots spaces and numbers: 1424848   ']

TEST_BOOLEANS: list[bool] = [True, False]

TEST_LISTS: list[list] = [[1, -2, 3], [], ['string test   ', 4, 5.0, False], [[5, 6], [], [True, False]]]

TEST_DICTIONARIES: list[dict] = [{}, {'a': 'b', 'c': 'd'}, {'a': 25.5, 'b': False, 'c': None, 'd': '  string  '},
                                 {'type': 'int', 'value': 5}]

TEST_TUPLES: list[tuple] = [(1, 2, 3), (True, '2022 test', 5), (), (5, 7, 5.2, False)]

SOME_MORE_COMPLEX: list = [
    [{'a': 2022, 'b': 4, 'c': 20, 'd': False}, True, None, 2022.0001],
    {'field1': True, 'field2': [1, 2, 3, {'a': True}], 'field3': {'field3_1': '   2022.0420   ', 'field3_2': 19}},
    [[[5, 6], True], False, True, 2022, [{}, [], {'field': [1, 2, 3]}], None, {'key': None}],
    [('key with value', [1]), {'author': 'User2022', 'message': 'Hi there ! How are you ? Greetings from April, 2022'}]
]

GLOBAL_INT: int = 42


def SIMPLE_FUNCTION_1(a: int, b: int) -> int:
    return (a * b) + GLOBAL_INT

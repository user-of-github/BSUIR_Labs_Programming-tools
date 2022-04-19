TEST_INTS: list[int] = [1, 2, 3, 4, 0, -1, 19999, -2022, 2022, 123456789]

TEST_FLOATS: list[float] = [1.0005, -2.1234, 3.0258480, 2022.20222022, 6, 7, -8, 0, 0.000]

TEST_STRINGS: list[str] = ['', 'some string', 'string with spaces', '    ',
                           '   string with Lots spaces and numbers: 1424848   ']

TEST_BOOLEANS: list[bool] = [True, False]

TEST_LISTS: list[list] = [[1, -2, 3], [], ['string test   ', 4, 5.0, False], [[5, 6], [], [True, False]]]

TEST_DICTIONARIES: list[dict] = [{}, {'a': 'b', 'c': 'd'}, {'a': 25.5, 'b': False, 'c': None, 'd': '  string  '}]

TEST_TUPLES: list[tuple] = [(1, 2, 3), (True, '2022 test', 5), (), (5, 7, 5.2, False)]

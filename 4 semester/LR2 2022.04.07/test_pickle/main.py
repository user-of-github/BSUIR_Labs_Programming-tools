import jsonpickle
import cloudpickle


def number_serialization_example() -> None:
    test_int_numbers: list[int] = [1, 2, 3, -5, 1000, -2022, 999999]
    test_float_numbers: list[int] = [1, 2.0005, 3.0, -5, 1000, -2022.157858, 999999.555]

    for number in test_int_numbers:
        print(jsonpickle.encode(number))

    for number in test_float_numbers:
        print(jsonpickle.encode(number))


def string_serialization_example() -> None:
    test_stings: list[str] = ['test', 'test with spaces   ',  'Some more test from 07.04.2022']

    for string in test_stings:
        print(jsonpickle.encode(string))


def class_serialization_example() -> None:
    def test_function(parameter) -> None:
        print(parameter)

    #print(cloudpickle.dumps(test_function))
    #print(test_function)

    #for field in dir(test_function):
    #    print(field, test_function.__getattribute__(field))


def array_serialization_example() -> None:
    test_int_numbers: list[int] = [1, 2, 3, -5, 1000, -2022, 999999]
    test_float_numbers: list[int] = [1, 2.0005, 3.0, -5, 1000, -2022.157858, 999999.555]
    test_strings: list[str] = ['test', 'test with spaces   ', 'Some more test from 07.04.2022']

    print(jsonpickle.encode(test_float_numbers))
    print(jsonpickle.encode(test_int_numbers))
    print(jsonpickle.encode(test_strings))


def main() -> None:
    number_serialization_example()
    string_serialization_example()
    class_serialization_example()
    array_serialization_example()


if __name__ == '__main__':
    main()

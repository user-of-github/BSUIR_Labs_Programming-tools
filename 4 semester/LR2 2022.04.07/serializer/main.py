from library.json.serialization_of_primitives.serialize_primitives import auto_serialize


def main() -> None:
    test_dict: dict = dict()
    test_dict['kek'] = 'shrek'
    test_dict['kek2'] = 'shrek2'
    test_dict['kek3'] = [4, 5, 6, "555"]
    test_dict[6] = [4, 5, 6, "555"]

    print(auto_serialize(test_dict))


if __name__ == '__main__':
    main()

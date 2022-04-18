from library.ipickler import IPickler
from library.pickler import Pickler
from library.pickler import PicklerType


def main() -> None:
    json_serializer: IPickler = Pickler.create_serializer(PicklerType.JSON)
    c = 42

    test_dict: dict = {
        'a': 5,
        'c': [5, 6, 7]
    }

    res = json_serializer.loads(json_serializer.dumps([['a', 'b', 2022], 6, 7]))
    print('____________________')
    for key in res['value']:
        print(key)


if __name__ == '__main__':
    main()

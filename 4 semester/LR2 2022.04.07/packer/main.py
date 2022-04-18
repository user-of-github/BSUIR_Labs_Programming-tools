from library.ipacker import IPacker
from library.packer import Packer
from library.packer import PackerType


def main() -> None:
    json_serializer: IPacker = Packer.create_serializer(PackerType.JSON)
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

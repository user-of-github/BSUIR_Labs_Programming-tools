from library.formats.dictionary.dictionary_encoder import DictionaryEncoder
from library.ipacker import IPacker
from library.packer import Packer
from library.packer import PackerType


def main() -> None:
    json_serializer: IPacker = Packer.create_serializer(PackerType.JSON)

    test_dict: dict = {
        'a': 5,
        'c': [5, 6, 7],
        'key': True,
        '5': {'a': False}
    }

    def test() -> None:
        print(42)

    array = [True, 2, 3, 4]
    json = json_serializer.dumps(array)
    print(json)
    print(json_serializer.loads(json))



if __name__ == '__main__':
    main()

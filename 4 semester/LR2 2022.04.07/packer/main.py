from library.formats.dictionary.dictionary_encoder import DictionaryEncoder
from library.ipacker import IPacker
from library.packer import Packer
from library.packer import PackerType


def main() -> None:
    json_serializer: IPacker = Packer.create_serializer(PackerType.JSON)

    test_dict: dict = {
        'a': 5,
        'c': [5, 6, 7]
    }

    print(DictionaryEncoder.auto_encode_to_dictionary(test_dict)
          == json_serializer.loads(json_serializer.dumps(test_dict)))


if __name__ == '__main__':
    main()

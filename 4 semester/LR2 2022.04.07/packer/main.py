import math
from library.ipacker import IPacker
from library.packer import Packer
from library.packer import PackerType


def main() -> None:
    json_packer: IPacker = Packer.create_serializer(PackerType.JSON)

    c: int = 42

    def test() -> None:
        print(c)
        print(math.pi)

    json_packer.dump(test, 'test_output.json')
    parsed = json_packer.load('test_output.json')
    print(parsed)


if __name__ == '__main__':
    main()

import math
import types

from library.ipacker import IPacker
from library.packer import Packer
from library.packer import PackerType
from library.utils.constants import ATTRIBUTES_OF_CODE_ATTRIBUTE


def main() -> None:
    json_packer: IPacker = Packer.create_serializer(PackerType.JSON)

    c: int = 42

    def test(a: int) -> int:
        return a

    json_packer.dump(test, 'test_output.json')
    parsed = json_packer.load('test_output.json')



    print(func(100))


if __name__ == '__main__':
    main()

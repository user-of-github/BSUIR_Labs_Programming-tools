import importlib

from library.ipacker import IPacker
from library.packer import Packer
from library.packer import PackerType
from library.utils.constants import ATTRIBUTES_OF_CODE_ATTRIBUTE



def main() -> None:
    json_packer: IPacker = Packer.create_serializer(PackerType.JSON)



    def test(a: float) -> None:
        print(c)

    json_packer.dump(test, 'test_output.json')

    func = json_packer.load('test_output.json')


if __name__ == '__main__':
    main()

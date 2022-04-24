import types

from library.ipacker import IPacker
from library.packer import Packer
from library.packer import PackerType


class Test:
    def __init__(self, name: str):
        self.name = name

    def test(self):
        print(self.name)
        print(42)

    def __private(self):
        print(42)


def main() -> None:
    json_packer: IPacker = Packer.create_serializer(PackerType.JSON)

    json_packer.dump(Test, 'test_output.json')
    MyNewDeserializedClass = json_packer.load('test_output.json')

    instance = MyNewDeserializedClass('SomeName')
    instance.test()


if __name__ == '__main__':
    main()

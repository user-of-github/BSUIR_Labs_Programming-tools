from library.ipacker import IPacker
from library.packer import Packer
from library.packer import PackerType


GLOBAL_INT: int = 4


def test(a: float) -> None:
    print(GLOBAL_INT)
    print(4)


def main() -> None:
    json_packer: IPacker = Packer.create_serializer(PackerType.JSON)



    json_packer.dump(test, 'test_output.json')

    func = json_packer.load('test_output.json')
    func(5)

if __name__ == '__main__':
    main()

import types

from library.ipacker import IPacker
from library.packer import Packer
from library.packer import PackerType

class Test:
    static_var_example = 42

    def __init__(self, name: str, age: int):
        self.__name = name
        self._age = age

    def foo(self):
        print('hello from foo !')
        self.some_funct()

    def some_funct(self):
        print('Hello from some_funct !, ', self.__name)

    def __str__(self):
        return f'Person: name = {self.__name}, age: {self._age}'


def main() -> None:
    json_packer: IPacker = Packer.create_serializer(PackerType.JSON)

    json_packer.dump(Test, 'test_output.json')

    Cl = json_packer.load('test_output.json')

    kek = Cl('kek', 52)
    print(kek)


if __name__ == '__main__':
    main()

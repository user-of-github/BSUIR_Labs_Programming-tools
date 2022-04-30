from packer.ipacker import IPacker
from packer.packer_main import Packer
from packer.packer_main import PackerType


class Test:
    static_var_example = 42

    def __init__(self, name: str, age: int):
        self.__name = name
        self.age = age

    def foo(self):
        print('hello from foo !')
        self.some_funct()

    def some_funct(self):
        print('Hello from some_funct !, ', self.__name)

    def __str__(self):
        self.kek = 'kek'
        return f'Person: name = {self.__name}, age: {self.age}'


def main() -> None:
    yaml_packer: IPacker = Packer.create_serializer(PackerType.YAML)
    json_packer: IPacker = Packer.create_serializer(PackerType.JSON)
    toml_packer: IPacker = Packer.create_serializer(PackerType.TOML)

    json_packer.dump(Test, 'test_output.json')


if __name__ == '__main__':
    main()

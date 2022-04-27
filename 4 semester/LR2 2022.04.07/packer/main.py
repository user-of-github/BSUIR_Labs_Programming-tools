from packer.ipacker import IPacker
from packer.packer import Packer
from packer.packer import PackerType


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

    '''json_packer.dump(Test, 'test_output.json')

    kek = Test('name', 2)
    print(kek)

    json_packer.dump(kek, 'test_output.json')
    kek2 = json_packer.load('test_output.json')

    kek.age = 10
    print(kek2, kek)
    '''

    arr = [1, 2, 3, [1, 2, 3, []], None]

    #toml.dump(5, 'test_output.toml')
    #print(toml.load('test_output.toml'))


if __name__ == '__main__':
    main()

from library.iserializer import ISerializer
from library.pickler import Pickler
from library.pickler import SerializerType

c: int = 52


def main() -> None:
    json_serializer: ISerializer = Pickler.create_serializer(SerializerType.JSON)
    yaml_serializer: ISerializer = Pickler.create_serializer(SerializerType.YAML)
    toml_serializer: ISerializer = Pickler.create_serializer(SerializerType.TOML)

    def test_funct(a: int = 410, b: int = 55) -> float:
        print(c)
        return a + b / 10 + c

    # print(json_serializer.dumps(test_funct))

    json_serializer.dump({'kek': 'shrek', 'nigga': {5: 6}}, 'output.json')
    print(bool('True') == 1)


if __name__ == '__main__':
    main()

from library.iserializer import ISerializer
from library.packer import Packer
from library.packer import SerializerType

c: int = 52

def main() -> None:
    json_serializer: ISerializer = Packer.create_serializer(SerializerType.JSON)
    yaml_serializer: ISerializer = Packer.create_serializer(SerializerType.YAML)
    toml_serializer: ISerializer = Packer.create_serializer(SerializerType.TOML)



    def test_funct(a: int = 410, b: int = 55) -> float:
        return a + b / 10 + c

    print(json_serializer.dumps(test_funct))


if __name__ == '__main__':
    main()

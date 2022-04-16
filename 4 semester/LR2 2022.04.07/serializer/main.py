from library.iserializer import ISerializer
from library.serializer import Serializer
from library.serializer import SerializerType


def main() -> None:
    serializer: ISerializer = Serializer.create_serializer(SerializerType.JSON)

    def test_function(a: int, b: float = 58) -> float:
        print(a, b)
        return a + b

    print(serializer.dumps(test_function))


if __name__ == '__main__':
    main()

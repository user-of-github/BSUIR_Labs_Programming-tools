import types

from library.iserializer import ISerializer
from library.serializer import Serializer
from library.serializer import SerializerType


def main() -> None:
    test_dict: dict = dict()
    test_dict['kek'] = 'shrek'
    test_dict['kek2'] = 'shrek2'
    test_dict['kek3'] = [4, 5, 6, "555"]
    test_dict[6] = [4, 5, 6, "555"]

    test_object: ISerializer = Serializer.create_serializer(SerializerType.JSON)

    def test_function(a: int, b: float) -> float:
        print(a, b)
        return a + b

    print(types.FunctionType, (test_function.__code__, {}, test_function.__name__,
                               test_function.__defaults__, test_function.__closure__),
          test_function.__dict__)


if __name__ == '__main__':
    main()

from enum import Enum
from library.iserializer import ISerializer
from library.json.json import Json
from library.yaml.yaml import Yaml
from library.toml.toml import Toml


class SerializerType(Enum):
    JSON = 1
    YAML = 2
    TOML = 3


class Serializer:
    @staticmethod
    def create_serializer(serializer_type: SerializerType) -> ISerializer:
        if serializer_type == SerializerType.JSON:
            return Json()
        elif serializer_type == SerializerType.YAML:
            return Yaml()
        elif serializer_type == SerializerType.TOML:
            return Toml()
        else:
            raise Exception('Invalid serializer type')

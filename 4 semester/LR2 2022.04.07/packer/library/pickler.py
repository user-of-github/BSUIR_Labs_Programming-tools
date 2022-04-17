from enum import Enum
from library.iserializer import ISerializer
from library.formats.json.json_pickler import JsonPickler
from library.formats.yaml.yaml_packer import YamlPacker
from library.formats.toml.toml_packer import TomlPacker


class SerializerType(Enum):
    JSON = 1
    YAML = 2
    TOML = 3


class Pickler:
    @staticmethod
    def create_serializer(serializer_type: SerializerType) -> ISerializer:
        if serializer_type == SerializerType.JSON:
            return JsonPickler()
        elif serializer_type == SerializerType.YAML:
            return YamlPacker()
        elif serializer_type == SerializerType.TOML:
            return TomlPacker()
        else:
            raise Exception('Invalid serializer type')

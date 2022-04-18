from enum import Enum
from library.ipickler import IPickler
from library.formats.json.json_pickler import JsonPickler
from library.formats.yaml.yaml_packer import YamlPacker
from library.formats.toml.toml_packer import TomlPacker


class PicklerType(Enum):
    JSON = 1
    YAML = 2
    TOML = 3


class Pickler:
    @staticmethod
    def create_serializer(serializer_type: PicklerType = PicklerType.JSON) -> IPickler:
        if serializer_type == PicklerType.JSON:
            return JsonPickler()
        elif serializer_type == PicklerType.YAML:
            return YamlPacker()
        elif serializer_type == PicklerType.TOML:
            return TomlPacker()
        else:
            raise Exception(f'Pickler error: {serializer_type} is invalid serializer type')

from enum import Enum
from packer.ipacker import IPacker
from packer.formats.json.json_packer import JsonPacker
from packer.formats.yaml.yaml_packer import YamlPacker
from packer.formats.toml.toml_packer import TomlPacker


class PackerType(Enum):
    JSON = 1
    YAML = 2
    TOML = 3


class Packer:
    @staticmethod
    def create_serializer(serializer_type: PackerType = PackerType.JSON) -> IPacker:
        if serializer_type == PackerType.JSON:
            return JsonPacker()
        elif serializer_type == PackerType.YAML:
            return YamlPacker()
        elif serializer_type == PackerType.TOML:
            return TomlPacker()
        else:
            raise Exception(f'Packer error: {serializer_type} is invalid serializer type')

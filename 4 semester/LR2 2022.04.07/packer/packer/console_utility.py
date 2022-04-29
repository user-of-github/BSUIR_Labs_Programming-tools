import argparse
from packer.ipacker import IPacker
from packer.packer import Packer, PackerType


def get_packer_instance(packer_type_source: str) -> IPacker:
    packer_type: str = packer_type_source.lower().strip()

    if packer_type == 'json':
        return Packer.create_serializer(PackerType.JSON)
    elif packer_type == 'yaml':
        return Packer.create_serializer(PackerType.YAML)
    elif packer_type == 'toml':
        return Packer.create_serializer(PackerType.TOML)
    else:
        return Packer.create_serializer(None)


def main() -> None:
    parser = argparse.ArgumentParser(description='Console utility converter for my Packer-Library')

    parser.add_argument('filefrom', type=str, help='Filename from')
    parser.add_argument('fileto', type=str, help='Filename from')
    parser.add_argument('formatfrom', type=str, help='Filename from')
    parser.add_argument('formatto', type=str, help='Filename from')

    args = parser.parse_args()

    deserializer: IPacker = get_packer_instance(args.formatfrom)
    serializer: IPacker = get_packer_instance(args.formatto)

    serializer.dump(deserializer.load(args.filefrom), args.fileto)

import argparse
from packer.ipacker import IPacker
from packer.packer_main import PackerType, Packer


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


parser = argparse.ArgumentParser(description='Console utility converter for my Packer-Library')

parser.add_argument('file_from', type=str, help='Filename from')
parser.add_argument('file_to', type=str, help='Filename from')
parser.add_argument('format_from', type=str, help='Filename from')
parser.add_argument('format_to', type=str, help='Filename from')

args = parser.parse_args()

deserializer: IPacker = get_packer_instance(args.format_from)
serializer: IPacker = get_packer_instance(args.format_to)

serializer.dump(deserializer.load(args.file_from), args.file_to)

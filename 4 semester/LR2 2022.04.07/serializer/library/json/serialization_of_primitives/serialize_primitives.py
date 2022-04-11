from typing import Union
from library.json.serialization_of_primitives.serialize_basic_primitive import serialize_basic_primitive
from library.utils.define_type import is_primitive, is_list, is_dict


def auto_serialize(to_serialize: Union[int, float, str, bool, list, dict]) -> str:
    if is_primitive(to_serialize):
        return serialize_basic_primitive(to_serialize)
    elif is_list(to_serialize):
        return serialize_list(to_serialize)
    elif is_dict(to_serialize):
        return serialize_dictionary(to_serialize)


def serialize_list(array: list) -> str:
    array_of_serialized_values: list = list()

    for item in array:
        array_of_serialized_values.append(auto_serialize(item))

    return '[' + ','.join(array_of_serialized_values) + ']'


def serialize_dictionary(dictionary: dict) -> str:
    array_of_serializes_fields: list[str] = list()

    for key in dictionary.keys():
        array_of_serializes_fields.append(f'{auto_serialize(str(key))}: {auto_serialize(dictionary.get(key))}')

    return '{' + ','.join(array_of_serializes_fields) + '}'

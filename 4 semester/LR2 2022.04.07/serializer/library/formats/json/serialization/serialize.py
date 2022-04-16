import inspect
from typing import Union

from library.formats.json.serialization.serialize_basic_primitive import serialize_basic_primitive, serialize_none
from library.utils.define_type import is_primitive, is_list, is_dict, is_function, is_none
import library.utils.constants as constants


class JsonSerializer:
    @staticmethod
    def auto_serialize(to_serialize) -> str:
        if is_primitive(to_serialize):
            return serialize_basic_primitive(to_serialize)
        elif is_list(to_serialize):
            return JsonSerializer.serialize_list(to_serialize)
        elif is_dict(to_serialize):
            return JsonSerializer.serialize_dictionary(to_serialize)
        elif is_function(to_serialize):
            return JsonSerializer.serialize_function(to_serialize)
        elif is_none(to_serialize):
            return JsonSerializer.serialize_none(to_serialize)

    @staticmethod
    def serialize_list(array: list) -> str:
        array_of_serialized_values: list = list()

        for item in array:
            array_of_serialized_values.append(JsonSerializer.auto_serialize(item))

        return ('{' +
                f'"type":"{constants.LIST_DESIGNATION}"'
                f',' +
                '"value":' + '[' + ','.join(array_of_serialized_values) + ']' +
                '}')

    @staticmethod
    def serialize_dictionary(dictionary: dict) -> str:
        array_of_serializes_fields: list[str] = list()

        for key in dictionary.keys():
            array_of_serializes_fields.append(
                f'{JsonSerializer.auto_serialize(str(key))}: {JsonSerializer.auto_serialize(dictionary.get(key))}')

        return '{' + ','.join(array_of_serializes_fields) + '}'

    @staticmethod
    def serialize_function(function) -> str:
        all_members: list = inspect.getmembers(function)

        necessary_members: list = list(filter(lambda item: item[0] in constants.ATTRIBUTES_OF_FUNCTION, all_members))

        for member in necessary_members:
            key: str = serialize_basic_primitive(member[0])

        response: str = JsonSerializer.serialize_dictionary({
            'type': constants.FUNCTION_DESIGNATION,
            'value': []
        })

        return response

    @staticmethod
    def serialize_basic_primitive(to_serialize: Union[int, float, str, bool]) -> str:
        if isinstance(to_serialize, str):
            return f'"{to_serialize}"'
        else:
            return f'{to_serialize}'

    @staticmethod
    def serialize_none(none: None) -> str:
        return (
                '{'
                + f'type:{constants.NONE_DESIGNATION},'
                + f'value:{none}'
                + '}'
        )

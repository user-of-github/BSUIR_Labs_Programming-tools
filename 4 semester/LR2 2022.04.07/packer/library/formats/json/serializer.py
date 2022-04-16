import builtins
import inspect
from typing import Union
from library.utils.define_type import is_primitive, is_list, is_dict, is_function, is_none
import library.utils.constants as constants


class JsonSerializer:
    @staticmethod
    def auto_serialize(to_serialize) -> str:
        if is_primitive(to_serialize):
            return JsonSerializer.serialize_basic_primitive(to_serialize)
        elif is_list(to_serialize):
            return JsonSerializer.serialize_list(to_serialize)
        elif is_dict(to_serialize):
            return JsonSerializer.serialize_dictionary(to_serialize)
        elif is_function(to_serialize):
            return JsonSerializer.serialize_function(to_serialize)

    @staticmethod
    def serialize_list(array: list) -> str:
        array_of_serialized_values: list = list()

        for item in array:
            array_of_serialized_values.append(JsonSerializer.auto_serialize(item))

        return ('{' +
                f'"type":"{constants.LIST_DESIGNATION}"'
                f',' +
                '"value":' +
                '[' + ','.join(array_of_serialized_values) + ']' +
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
        print('Serializing func !')
        dictionary_with_attributes: dict = JsonSerializer.__transform_function_to_dictionary(function)

        response: str = JsonSerializer.serialize_dictionary({
            'type': constants.FUNCTION_DESIGNATION,
            'value': dictionary_with_attributes
        })

        return response

    @staticmethod
    def serialize_basic_primitive(to_serialize: Union[int, float, str, bool, None]) -> str:
        if isinstance(to_serialize, str):
            return f'"{to_serialize}"'
        elif to_serialize is None:
            return 'null'
        else:
            return f'{to_serialize}'

    @staticmethod
    def __transform_function_to_dictionary(function) -> dict:
        attributes: dict = {
            '__name__': function.__qualname__,
            '__defaults__': function.__defaults__,
            '__closure__': function.__closure__,
            '__code__': function.__code__
        }

        function_globals: dict = dict()
        JsonSerializer.__get_closure_globals(function, function_globals)

        response: dict = {
            'attributes': attributes,
            '__globals__': function_globals
        }

        return response

    @staticmethod
    def __get_closure_globals(item, globals_response: dict) -> None:
        if hasattr(item, '__code__'):
            code_object = item.__code__

            for co_const in code_object.co_consts:
                JsonSerializer.__get_closure_globals(co_const, globals_response)

            for co_name in code_object.co_names:
                if co_name in item.__globals__.keys() and co_name != item.__name__:
                    globals_response[co_name] = item.__globals__[co_name]
                elif co_name in dir(builtins):
                    globals_response[co_name] = getattr(builtins, co_name)

import builtins
import importlib
import types
from typing import Union

from library.utils import constants


class DictionaryDecoder:
    @staticmethod
    def auto_decode_to_object(source: dict):
        if source['type'] == constants.INT_DESIGNATION:
            return source['value']
        elif source['type'] == constants.FLOAT_DESIGNATION:
            return source['value']
        elif source['type'] == constants.STR_DESIGNATION:
            return str(source['value']).replace(constants.SYMBOLS_TO_REPLACE_SPACE_IN_STRINGS, ' ')
        elif source['type'] == constants.BOOL_DESIGNATION:
            return source['value']
        elif source['type'] == constants.NONE_DESIGNATION:
            return None
        elif source['type'] == constants.LIST_DESIGNATION or source['type'] == constants.TUPLE_DESIGNATION:
            return DictionaryDecoder.__decode_list_or_tuple(source)
        elif source['type'] == constants.DICTIONARY_DESIGNATION:
            return DictionaryDecoder.__decode_dictionary(source['value'])
        elif source['type'] == constants.FUNCTION_DESIGNATION:
            return DictionaryDecoder.__decode_function(source)
        elif source['type'] == constants.BYTES_DESIGNATION:
            return bytes.fromhex(source['value'])
        elif source['type'] == constants.CODE_DESIGNATION:
            return DictionaryDecoder.__decode_code_type(source['value'])
        elif source['type'] == constants.CLASS_DESIGNATION:
            return DictionaryDecoder.__decode_class(source['value'])
        elif source['type'] == constants.INSTANCE_DESIGNATION:
            return DictionaryDecoder.__decode_instance(source['value'])
        else:
            raise Exception(f'DictionaryDecoder error: unknown type: {source["type"]}')

    @staticmethod
    def __decode_list_or_tuple(source: dict) -> Union[list, tuple]:
        response: list = list()

        for item in source['value']:
            response.append(DictionaryDecoder.auto_decode_to_object(item))

        if source['type'] == constants.TUPLE_DESIGNATION:
            return tuple(response)
        else:
            return response

    @staticmethod
    def __decode_dictionary(source: dict) -> dict:
        response: dict = dict()

        for key in source:
            response[key] = DictionaryDecoder.auto_decode_to_object(source[key])

        return response

    @staticmethod
    def __decode_function(source: dict) -> types.FunctionType:
        function_dictionary: dict = DictionaryDecoder.__decode_dictionary(source['value']['value']['value']['value'])

        function_name: str = DictionaryDecoder.auto_decode_to_object(function_dictionary['__name__'])

        code: types.CodeType = DictionaryDecoder.auto_decode_to_object({
            'type': constants.CODE_DESIGNATION,
            'value': function_dictionary['__code__']['value']
        })

        for module_name in DictionaryDecoder.auto_decode_to_object(function_dictionary['__globals__'])['__modules']:
            builtins.__dict__[module_name] = importlib.import_module(module_name)

        globals_dict: dict = DictionaryDecoder.__decode_dictionary(function_dictionary['__globals__']['value'])
        globals_dict['__builtins__'] = __builtins__

        return types.FunctionType(code, globals_dict, function_name)

    @staticmethod
    def __decode_code_type(source: dict) -> types.CodeType:
        code_object: list = list()

        for attr in constants.ATTRIBUTES_OF_CODE_TYPE:
            code_object.append(DictionaryDecoder.auto_decode_to_object(source[attr]))

        response: types.CodeType = types.CodeType(*code_object)

        return response

    @staticmethod
    def __decode_class(initial_source: dict):
        source: dict = initial_source['value']

        name: str = DictionaryDecoder.auto_decode_to_object(source['name'])

        decoded_functions = DictionaryDecoder.__decode_list_or_tuple(source['methods'])

        methods_and_static_vars: dict = dict()

        decoded_static_variables: dict = DictionaryDecoder.auto_decode_to_object(source['static_variables'])
        for static in decoded_static_variables:
            methods_and_static_vars[static] = decoded_static_variables[static]

        for method in decoded_functions:
            methods_and_static_vars[method.__name__] = method

        response = type(name, (), methods_and_static_vars)

        return response

    @staticmethod
    def __decode_instance(source: dict):
        decoded_class = DictionaryDecoder.auto_decode_to_object(source['class'])
        decoded_params = DictionaryDecoder.auto_decode_to_object(source['fields'])

        return decoded_class(*decoded_params)
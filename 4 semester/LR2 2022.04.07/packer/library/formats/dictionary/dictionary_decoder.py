import builtins
import importlib
import types
from typing import Union

from library.utils import constants


class DictionaryDecoder:
    @staticmethod
    def auto_decode_to_object(source: dict):
        if not source:
            return None

        if 'type' not in source:
            return DictionaryDecoder.__decode_dictionary(source)

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
        elif source['type'] == constants.CELL_DESIGNATION:
            return None
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
    def __decode_function(source: dict):
        data_to_create_function: dict = DictionaryDecoder.auto_decode_to_object({
            'type': 'dict',
            'value': DictionaryDecoder.auto_decode_to_object(source['value']['value']['value'])
        })

        code_object: list = list()
        for attr in constants.ATTRIBUTES_OF_CODE_ATTRIBUTE:
            code_object.append(data_to_create_function['__code__'][attr])

        code: types.CodeType = types.CodeType(*code_object)

        for module_name in data_to_create_function['__globals__']['__modules']:
            builtins.__dict__[module_name] = importlib.import_module(module_name)

        globals_dict: dict = data_to_create_function['__globals__']
        globals_dict['__builtins__'] = __builtins__

        return types.FunctionType(code, globals_dict)

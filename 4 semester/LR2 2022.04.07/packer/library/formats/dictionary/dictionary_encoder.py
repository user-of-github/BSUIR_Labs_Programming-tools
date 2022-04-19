import builtins
import inspect
import types
from typing import Union

from library.utils import constants
from library.utils.define_type import DefineType


class DictionaryEncoder:
    @staticmethod
    def auto_encode_to_dictionary(to_serialize) -> dict:
        if DefineType.is_primitive(to_serialize):
            return DictionaryEncoder.encode_basic_primitive(to_serialize)
        elif DefineType.is_list_or_tuple(to_serialize):
            return DictionaryEncoder.encode_list_or_tuple(to_serialize)
        elif DefineType.is_dict(to_serialize):
            return DictionaryEncoder.encode_dictionary(to_serialize)
        elif DefineType.is_function(to_serialize):
            return DictionaryEncoder.encode_function(to_serialize)

    @staticmethod
    def encode_basic_primitive(to_serialize: Union[int, float, str, bool, None]) -> dict:
        response: dict = dict()

        response['type'] = DictionaryEncoder.__get_primitive_type_name(to_serialize)
        response['value'] = DictionaryEncoder.__get_value_for_primitive(to_serialize)

        return response

    @staticmethod
    def encode_list_or_tuple(array: Union[list, tuple]) -> dict:
        response: dict = dict()

        if isinstance(array, list):
            response['type'] = constants.LIST_DESIGNATION
        elif isinstance(array, tuple):
            response['type'] = constants.TUPLE_DESIGNATION
        else:
            raise Exception(f'Converter error: {array} is not a list or tuple')

        response['value'] = list()

        for value in array:
            response['value'].append(DictionaryEncoder.auto_encode_to_dictionary(value))

        return response

    @staticmethod
    def encode_dictionary(dictionary: dict) -> dict:
        response: dict = dict()

        response['type'] = constants.DICTIONARY_DESIGNATION
        response['value'] = dict()

        for key in dictionary.keys():
            response['value'][str(key)] = DictionaryEncoder.auto_encode_to_dictionary(dictionary.get(key))

        return response

    @staticmethod
    def encode_function(function) -> dict:
        response: dict = dict()

        response['type'] = constants.FUNCTION_DESIGNATION
        response['value'] = DictionaryEncoder.encode_dictionary(
            DictionaryEncoder.__transform_function_to_dictionary(function))

        return response

    @staticmethod
    def __get_value_for_primitive(to_serialize: Union[int, float, str, bool, None]):
        if isinstance(to_serialize, bool) or (to_serialize is None):
            return str(to_serialize)
        elif isinstance(to_serialize, str):
            return to_serialize.replace(' ', constants.SYMBOLS_TO_REPLACE_SPACE_IN_STRINGS)
        else:
            return to_serialize

    @staticmethod
    def __get_primitive_type_name(primitive: Union[int, float, str, bool, None]) -> str:
        if isinstance(primitive, bool):
            return constants.BOOL_DESIGNATION
        elif isinstance(primitive, float):
            return constants.FLOAT_DESIGNATION
        elif isinstance(primitive, str):
            return constants.STR_DESIGNATION
        elif isinstance(primitive, int):
            return constants.INT_DESIGNATION
        elif primitive is None:
            return constants.NONE_DESIGNATION
        else:
            raise Exception(f'Converter error: {primitive} is not a primitive')

    @staticmethod
    def __transform_function_to_dictionary(obj) -> dict:
        body: dict = dict()

        body["type"] = "function"
        body["value"] = {}
        all_arguments = inspect.getmembers(obj)
        code_all_arguments = inspect.getmembers(obj.__code__)
        arguments = [argument for argument in all_arguments if argument[0] in constants.ATTRIBUTES_OF_FUNCTION]
        code_args = [code_argument for code_argument in code_all_arguments if
                     code_argument[0] in constants.ATTRIBUTES_OF_CODE_ATTRIBUTE]
        for argument in arguments:
            if argument[0] != "__code__":
                body["value"].update({argument[0]: DictionaryEncoder.auto_encode_to_dictionary(argument[1])})
            else:
                body["value"].update({"__code__": {}})
                for code_arg in code_args:
                    body["value"]["__code__"].update(
                        {code_arg[0]: DictionaryEncoder.auto_encode_to_dictionary(code_arg[1])})

        globs_vals = {}
        globs = obj.__getattribute__("__globals__")
        func_glob_args = obj.__code__.co_names
        modules_names = []
        for func_glob_arg in func_glob_args:
            if func_glob_arg in globs:
                if isinstance(globs[func_glob_arg], types.ModuleType):
                    modules_names.append(func_glob_arg)
                else:
                    globs_vals.update({func_glob_arg: globs[func_glob_arg]})

        globs_vals.update({"__modules": modules_names})
        globs_vals_serialized = DictionaryEncoder.auto_encode_to_dictionary(globs_vals)
        body["value"].update({"__globals__": globs_vals_serialized})

        return body

    @staticmethod
    def __get_closure_globals(item, globals_response: dict) -> None:
        if hasattr(item, '__code__'):
            code_object = item.__code__

            for co_const in code_object.co_consts:
                DictionaryEncoder.__get_closure_globals(co_const, globals_response)

            for co_name in code_object.co_names:
                if co_name in item.__globals__.keys() and co_name != item.__name__:
                    globals_response[co_name] = item.__globals__[co_name]
                elif co_name in dir(builtins):
                    globals_response[co_name] = getattr(builtins, co_name)

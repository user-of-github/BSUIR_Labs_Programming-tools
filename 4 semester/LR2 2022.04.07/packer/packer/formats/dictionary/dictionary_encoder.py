import inspect
import types
from typing import Union

from packer.utils import constants
from packer.utils.define_type import DefineType


class DictionaryEncoder:
    @staticmethod
    def auto_encode_to_dictionary(to_serialize) -> dict:
        if DefineType.is_primitive(to_serialize):
            return DictionaryEncoder.__encode_basic_primitive(to_serialize)
        elif DefineType.is_list_or_tuple(to_serialize):
            return DictionaryEncoder.__encode_list_or_tuple(to_serialize)
        elif DefineType.is_dict(to_serialize):
            return DictionaryEncoder.__encode_dictionary(to_serialize)
        elif DefineType.is_function(to_serialize):
            return DictionaryEncoder.__encode_function(to_serialize)
        elif DefineType.is_bytes(to_serialize):
            return DictionaryEncoder.__encode_bytes(to_serialize)
        elif DefineType.is_code(to_serialize):
            return DictionaryEncoder.__encode_code_type(to_serialize)
        elif DefineType.is_class(to_serialize):
            return DictionaryEncoder.__encode_custom_user_class(to_serialize)
        else:
            return DictionaryEncoder.__encode_instance(to_serialize)

    @staticmethod
    def __encode_basic_primitive(to_serialize: Union[int, float, str, bool, None]) -> dict:
        response: dict = dict()

        response['type'] = DictionaryEncoder.__get_primitive_type_name(to_serialize)
        response['value'] = DictionaryEncoder.__get_value_for_primitive(to_serialize)

        return response

    @staticmethod
    def __encode_list_or_tuple(array: Union[list, tuple]) -> dict:
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
    def __encode_dictionary(dictionary: dict) -> dict:
        response: dict = dict()

        response['type'] = constants.DICTIONARY_DESIGNATION
        response['value'] = dict()

        if dictionary:
            for key in dictionary.keys():
                response['value'][key] = DictionaryEncoder.auto_encode_to_dictionary(dictionary[key])

        return response

    @staticmethod
    def __encode_function(function) -> dict:
        response: dict = dict()

        response['type'] = constants.FUNCTION_DESIGNATION
        response['value'] = DictionaryEncoder.__encode_dictionary(
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
    def __transform_function_to_dictionary(function) -> dict:
        response: dict = dict()

        response['type'] = constants.FUNCTION_DESIGNATION
        response['value'] = dict()

        response['value']['__name__'] = DictionaryEncoder.auto_encode_to_dictionary(function.__name__)
        response['value']['__defaults__'] = DictionaryEncoder.auto_encode_to_dictionary(function.__defaults__)
        response['value']['__closure__'] = DictionaryEncoder.auto_encode_to_dictionary(function.__closure__)
        response['value']['__code__'] = DictionaryEncoder.auto_encode_to_dictionary(function.__code__)

        globs_vals: dict = dict()
        globs = function.__getattribute__('__globals__')

        modules_names: list = list()

        for func_glob_arg in function.__code__.co_names:
            if func_glob_arg in globs:
                if isinstance(globs[func_glob_arg], types.ModuleType):
                    modules_names.append(func_glob_arg)
                else:
                    globs_vals[func_glob_arg] = globs[func_glob_arg]

        globs_vals['__modules'] = modules_names
        response['value']['__globals__'] = DictionaryEncoder.auto_encode_to_dictionary(globs_vals)

        return response

    @staticmethod
    def __encode_bytes(bytes_object: Union[bytes, bytearray]) -> dict:
        response: dict = dict()

        response['type'] = constants.BYTES_DESIGNATION
        response['value'] = bytes_object.hex()

        return response

    @staticmethod
    def __encode_code_type(code: types.CodeType) -> dict:
        response: dict = dict()

        response['key'] = constants.CODE_DESIGNATION
        response['value'] = dict()

        code_args: list = list(filter(
            lambda arg: arg[0] in constants.ATTRIBUTES_OF_CODE_TYPE,
            inspect.getmembers(code)
        ))

        for code_arg in code_args:
            response['value'][code_arg[0]] = DictionaryEncoder.auto_encode_to_dictionary(code_arg[1])

        return response

    @staticmethod
    def __encode_custom_user_class(user_class) -> dict:
        response: dict = dict()

        methods_names: list = list(filter(
            lambda method: callable(getattr(user_class, method))
                           and method not in constants.UNNECESSARY_CLASS_ATTRIBUTES,
            dir(user_class)
        ))

        value: dict = dict()

        methods: list = list()

        for method_name in methods_names:
            methods.append(getattr(user_class, method_name))

        static_variables_names: list = list(filter(
            lambda static_var_name: not callable(getattr(user_class, static_var_name))
                                    and static_var_name not in constants.UNNECESSARY_CLASS_ATTRIBUTES,
            dir(user_class)
        ))

        static_variables: dict = dict()

        for var_name in static_variables_names:
            static_variables[var_name] = getattr(user_class, var_name)

        value['methods'] = methods
        value['name'] = user_class.__name__
        value['static_variables'] = static_variables

        response['type'] = constants.CLASS_DESIGNATION
        response['value'] = dict()
        response['value'] = DictionaryEncoder.auto_encode_to_dictionary(value)

        return response

    @staticmethod
    def __encode_instance(instance) -> dict:
        response: dict = dict()

        response['type'] = constants.INSTANCE_DESIGNATION
        response['value'] = dict()

        response['value']['class'] = DictionaryEncoder.auto_encode_to_dictionary(instance.__class__)

        fields: list = list()

        for code_arg in inspect.getmembers(instance.__class__.__init__.__code__):
            if code_arg[0] == 'co_names':
                for name in code_arg[1]:
                    fields.append(instance.__dict__[name])

                break

        response['value']['fields'] = DictionaryEncoder.auto_encode_to_dictionary(fields)

        return response
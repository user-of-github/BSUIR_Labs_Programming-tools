import builtins
import inspect
from typing import Union
from library.utils.define_type import DefineType
import library.utils.constants as constants


class JsonSerializer:
    @staticmethod
    def auto_serialize(to_serialize) -> str:
        return str(JsonSerializer.auto_pack_to_dictionary(to_serialize)).replace('\'', '"')

    @staticmethod
    def auto_pack_to_dictionary(to_serialize) -> dict:
        if DefineType.is_primitive(to_serialize):
            return JsonSerializer.pack_basic_primitive(to_serialize)
        elif DefineType.is_list_or_tuple(to_serialize):
            return JsonSerializer.pack_list_or_tuple(to_serialize)
        elif DefineType.is_dict(to_serialize):
            return JsonSerializer.pack_dictionary(to_serialize)
        elif DefineType.is_function(to_serialize):
            return JsonSerializer.pack_function(to_serialize)

    @staticmethod
    def pack_list_or_tuple(array: Union[list, tuple]) -> dict:
        response: dict = dict()

        if isinstance(array, list):
            response['type'] = constants.LIST_DESIGNATION
        elif isinstance(array, tuple):
            response['type'] = constants.TUPLE_DESIGNATION
        else:
            raise Exception(f'JsonSerializer error: {array} is not a list or tuple')

        response['value'] = list()

        for value in array:
            response['value'].append(JsonSerializer.auto_pack_to_dictionary(value))

        return response

    @staticmethod
    def pack_dictionary(dictionary: dict) -> dict:
        response: dict = dict()

        response['type'] = constants.DICTIONARY_DESIGNATION
        response['value'] = dict()

        for key in dictionary.keys():
            response['value'][str(key)] = JsonSerializer.auto_pack_to_dictionary(dictionary.get(key))

        return response

    @staticmethod
    def pack_function(function) -> str:
        print('Serializing func !')
        dictionary_with_attributes: dict = JsonSerializer.__transform_function_to_dictionary(function)

        response: str = JsonSerializer.serialize_dictionary({
            'type': constants.FUNCTION_DESIGNATION,
            'value': dictionary_with_attributes
        })

        return response

    @staticmethod
    def pack_basic_primitive(to_serialize: Union[int, float, str, bool, None]) -> dict:
        response: dict = dict()

        response['type'] = JsonSerializer.__get_primitive_type_name(to_serialize)
        response['value'] = JsonSerializer.__get_value_for_primitive(to_serialize)

        return response

    @staticmethod
    def __get_value_for_primitive(to_serialize: Union[int, float, str, bool, None]):
        if isinstance(to_serialize, bool) or to_serialize is None:
            return str(to_serialize)
        else:
            return to_serialize

    @staticmethod
    def __get_primitive_type_name(primitive: Union[int, float, str, bool, None]) -> str:
        if isinstance(primitive, int):
            return constants.INT_DESIGNATION
        elif isinstance(primitive, float):
            return constants.INT_DESIGNATION
        elif isinstance(primitive, str):
            return constants.INT_DESIGNATION
        elif isinstance(primitive, bool):
            return constants.INT_DESIGNATION
        elif primitive is None:
            return constants.NONE_DESIGNATION
        else:
            raise Exception(f'JsonSerializer error: {primitive} is not a primitive')

    @staticmethod
    def __transform_function_to_dictionary(function) -> dict:
        ans: dict = dict()
        ans["type"] = "function"
        ans["value"] = {}
        members = inspect.getmembers(function)
        members = [i for i in members if i[0] in constants.ATTRIBUTES_OF_FUNCTION]
        for i in members:
            key = JsonSerializer.auto_serialize(i[0])
            if i[0] != "__closure__":
                value = JsonSerializer.auto_serialize(i[1])
            else:
                value = JsonSerializer.auto_serialize(None)
            ans["value"][key] = value
            if i[0] == "__code__":
                key = JsonSerializer.auto_serialize("__globals__")
                ans["value"][key] = {}
                names = i[1].__getattribute__("co_names")
                glob = function.__getattribute__("__globals__")
                globdict = {}
                for name in names:
                    if name == function.__name__:
                        globdict[name] = function.__name__
                    elif name in glob and not inspect.ismodule(name) and name not in __builtins__:
                        globdict[name] = glob[name]
                ans["value"][key] = JsonSerializer.auto_serialize(globdict)
        ans["value"] = tuple((k, ans["value"][k]) for k in ans["value"])

        return ans

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

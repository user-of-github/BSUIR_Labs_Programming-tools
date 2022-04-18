import re

from library.utils import constants


class JsonParser:
    @staticmethod
    def auto_unpack_from_string_to_dictionary(string_source: str) -> dict:
        response: dict = dict()

        source: str = re.sub(re.compile(r'\s+'), '', string_source)

        object_type_str: str = re.findall('"type":"([a-z]+)"', source)[0]
        object_value_str: str = source[19 + len(object_type_str):len(source) - 1]

        response['type'] = object_type_str

        if object_type_str == constants.INT_DESIGNATION:
            response['value'] = int(object_value_str)
        elif object_type_str == constants.FLOAT_DESIGNATION:
            response['value'] = float
        elif object_type_str == constants.STR_DESIGNATION:
            response['value'] = object_value_str[1:-1]
        elif object_type_str == constants.BOOL_DESIGNATION:
            response['value'] = bool(object_value_str[1:-1])
        elif object_type_str == constants.NONE_DESIGNATION:
            response['value'] = None
        elif object_type_str == constants.LIST_DESIGNATION:
            response['value'] = list()
            splited_object_strings: list = JsonParser.__split_list_string_to_objects_strings(object_value_str)

            for object_string in splited_object_strings:
                response['value'].append(JsonParser.auto_unpack_from_string_to_dictionary(object_string))

        return response

    @staticmethod
    def __split_list_string_to_objects_strings(list_string: str) -> list[str]:
        source: str = list_string[1:-1]  # to put away '[' and ']'

        response: list = list()

        object_beginning_index: int = 0
        depth_level: int = 0

        for index in range(len(list_string)):
            if list_string[index] == '{':
                depth_level += 1
            elif list_string[index] == '}':
                depth_level -= 1

            if depth_level == 0 and index > object_beginning_index:
                response.append(source[object_beginning_index:index])
                object_beginning_index = index + 1

        return response

import re
from typing import Union

from library.utils import constants


class JsonParser:
    @staticmethod
    def auto_parse_from_string_to_dictionary(string_source: str) -> dict:
        response: dict = dict()

        source: str = re.sub(re.compile(r'\s+'), '', string_source)

        object_type_str: str = re.findall('"type":"([a-z]+)"', source)[0]
        object_value_str: str = source[19 + len(object_type_str):len(source) - 1]

        response['type'] = object_type_str

        if object_type_str == constants.INT_DESIGNATION:
            response['value'] = int(object_value_str)
        elif object_type_str == constants.FLOAT_DESIGNATION:
            response['value'] = float(object_value_str)
        elif object_type_str == constants.STR_DESIGNATION:
            response['value'] = object_value_str[1:-1]
        elif object_type_str == constants.BOOL_DESIGNATION:
            response['value'] = True if object_value_str[1:-1] == 'True' else False
        elif object_type_str == constants.NONE_DESIGNATION:
            response['value'] = None
        elif object_type_str == constants.LIST_DESIGNATION or object_type_str == constants.TUPLE_DESIGNATION:
            response['value'] = JsonParser.__parse_list_or_tuple(object_value_str, object_type_str)
        elif object_type_str == constants.DICTIONARY_DESIGNATION:
            response['value'] = JsonParser.__parse_dictionary(object_value_str)

        return response

    @staticmethod
    def __parse_list_or_tuple(object_value_str: str, object_type_str: str) -> Union[list, tuple]:
        splited_object_strings: list = JsonParser.__split_list_string_to_objects_strings(object_value_str)
        parsed_objects: list = list()

        for object_string in splited_object_strings:
            parsed_objects.append(JsonParser.auto_parse_from_string_to_dictionary(object_string))

        if object_type_str == constants.TUPLE_DESIGNATION:
            return tuple(parsed_objects)
        else:
            return list(parsed_objects)

    @staticmethod
    def __split_list_string_to_objects_strings(list_string: str) -> list[str]:
        source: str = list_string[1:-1]  # to put away '[' and ']'

        response: list = list()

        if source == '':
            return response

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

    @staticmethod
    def __parse_dictionary(dictionary_string: str) -> dict:
        source: str = dictionary_string[1:-1]  # to remove first and last '{', '}'
        parsed_into_pairs_key_value: list[str, str] = JsonParser.__split_dict_string_to_pair_of_key_value(source)

        response: dict = dict()

        for key, value in parsed_into_pairs_key_value:
            response[key] = JsonParser.auto_parse_from_string_to_dictionary(value)

        return response

    @staticmethod
    def __split_dict_string_to_pair_of_key_value(source: str) -> list[(str, str)]:
        response: list[(str, str)] = list()

        pair_beginning_index: int = 0
        quotes_count: int = 0
        depth_level: int = 0
        has_met_brackets: bool = False

        for index in range(len(source)):
            if source[index] == '{':
                depth_level += 1
                has_met_brackets = True
            elif source[index] == '}':
                depth_level -= 1
                has_met_brackets = True
            elif source[index] == '"':
                quotes_count += 1

            if depth_level == 0 and (quotes_count >= 2) and (index > pair_beginning_index) and has_met_brackets:
                single_pair_string: str = source[pair_beginning_index:index+1]
                key_string: str = re.findall('"([A-Za-z0-9]+)"', single_pair_string)[0]
                value_string: str = single_pair_string[3 + len(key_string):len(single_pair_string)]
                response.append((key_string, value_string))
                pair_beginning_index = index + 2
                quotes_count = 0
                has_met_brackets = False

        return response

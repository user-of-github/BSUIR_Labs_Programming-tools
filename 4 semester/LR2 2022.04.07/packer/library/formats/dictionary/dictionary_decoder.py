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
        elif source['type'] == constants.LIST_DESIGNATION or source['type'] == constants.TUPLE_DESIGNATION:
            return DictionaryDecoder.__decode_list_or_tuple(source)
        elif source['type'] == constants.DICTIONARY_DESIGNATION:
            return DictionaryDecoder.__decode_dictionary(source['value'])

    @staticmethod
    def __decode_list_or_tuple(source: dict) -> Union[list, tuple]:
        response: list = list()

        for obj in source['value']:
            response.append(DictionaryDecoder.auto_decode_to_object(obj))

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
from typing import Union

from library.utils import constants


class DictionaryDecoder:
    @staticmethod
    def auto_decode_to_object(source: dict):
        if not source:
            return None

        if 'type' in source and source['type'] == constants.INT_DESIGNATION:
            return source['value']
        elif 'type' in source and source['type'] == constants.FLOAT_DESIGNATION:
            return source['value']
        elif 'type' in source and source['type'] == constants.STR_DESIGNATION:
            return str(source['value']).replace(constants.SYMBOLS_TO_REPLACE_SPACE_IN_STRINGS, ' ')
        elif 'type' in source and source['type'] == constants.BOOL_DESIGNATION:
            return source['value']
        elif 'type' in source and source['type'] == constants.NONE_DESIGNATION:
            return None
        elif 'type' in source and (source['type'] == constants.LIST_DESIGNATION or source['type'] == constants.TUPLE_DESIGNATION):
            return DictionaryDecoder.__decode_list_or_tuple(source)
        elif 'type' in source and source['type'] == constants.DICTIONARY_DESIGNATION:
            return DictionaryDecoder.__decode_dictionary(source['value'])
        elif 'type' in source and source['type'] == constants.FUNCTION_DESIGNATION:
            return DictionaryDecoder.auto_decode_to_object({
                'type': 'dict',
                'value': DictionaryDecoder.auto_decode_to_object(source['value']['value']['value'])
            })
        elif 'type' in source:
            raise Exception(f'DictionaryDecoder error: unknown type: {source["type"]}')
        else:
            return DictionaryDecoder.__decode_dictionary(source)

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
            value = DictionaryDecoder.auto_decode_to_object(source[key])
            response[key] = value

        return response

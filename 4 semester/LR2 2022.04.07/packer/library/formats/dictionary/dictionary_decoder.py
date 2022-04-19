from library.utils import constants


class DictionaryDecoder:
    @staticmethod
    def auto_decode_to_object(source: dict):
        if source['type'] == constants.INT_DESIGNATION:
            return int(source['value'])
        elif source['type'] == constants.FLOAT_DESIGNATION:
            return float(source['value'])
        elif source['type'] == constants.STR_DESIGNATION:
            return str(source['value'])
        elif source['type'] == constants.BOOL_DESIGNATION:
            return bool(source['value'])
        elif source['type'] == constants.LIST_DESIGNATION:
            response: list = list()

            for obj in source['value']:
                response.append(DictionaryDecoder.auto_decode_to_object(obj))

            return response


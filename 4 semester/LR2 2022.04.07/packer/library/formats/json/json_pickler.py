from library.formats.dictionary.dictionary_encoder import DictionaryEncoder
from library.formats.json.parser import JsonParser
from library.ipickler import IPickler


class JsonPickler(IPickler):
    def dumps(self, object_to_serialize) -> str:
        return str(DictionaryEncoder.auto_pack_to_dictionary(object_to_serialize)).replace('\'', '"')

    def dump(self, object_to_serialize, file_name: str) -> None:
        file = open(file_name, 'w')
        file.write(str(DictionaryEncoder.auto_pack_to_dictionary(object_to_serialize)).replace('\'', '"'))
        file.close()

    def load(self, file_name: str):
        file = open(file_name, 'r')
        source: str = file.read()
        file.close()

    def loads(self, source: str):
        parsed_dictionary: dict = JsonParser.auto_unpack_from_string_to_dictionary(source)
        return parsed_dictionary

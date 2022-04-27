from packer.formats.dictionary.dictionary_decoder import DictionaryDecoder
from packer.formats.dictionary.dictionary_encoder import DictionaryEncoder
from packer.formats.json.json_parser import JsonParser
from packer.ipacker import IPacker


class JsonPacker(IPacker):
    def dumps(self, object_to_serialize) -> str:
        return str(DictionaryEncoder.auto_encode_to_dictionary(object_to_serialize)).replace('\'', '"')

    def dump(self, object_to_serialize, file_name: str) -> None:
        file = open(file_name, 'w')
        file.write(self.dumps(object_to_serialize))
        file.close()

    def loads(self, source: str):
        parsed_dictionary: dict = JsonParser.auto_parse_from_string_to_dictionary(source)

        return DictionaryDecoder.auto_decode_to_object(parsed_dictionary)

    def load(self, file_name: str):
        file = open(file_name, 'r')
        source: str = file.read()
        file.close()

        return self.loads(source)

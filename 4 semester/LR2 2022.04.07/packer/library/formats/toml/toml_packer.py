import toml

from library.formats.dictionary.dictionary_decoder import DictionaryDecoder
from library.formats.dictionary.dictionary_encoder import DictionaryEncoder
from library.ipacker import IPacker


class TomlPacker(IPacker):
    def dumps(self, object_to_serialize) -> str:
        return toml.dumps(DictionaryEncoder.auto_encode_to_dictionary(object_to_serialize))

    def dump(self, object_to_serialize, file_name: str) -> None:
        file = open(file_name, 'w+')
        file.write(self.dumps(object_to_serialize))
        file.close()

    def loads(self, source: str):
        return DictionaryDecoder.auto_decode_to_object(dict(toml.loads(source)))

    def load(self, file_name: str):
        file = open(file_name, 'r')
        source: str = file.read()
        file.close()

        return self.loads(source)

from packer.formats.dictionary.dictionary_decoder import DictionaryDecoder
from packer.formats.dictionary.dictionary_encoder import DictionaryEncoder
from packer.ipacker import IPacker
import yaml


class YamlPacker(IPacker):
    def dumps(self, object_to_serialize) -> str:
        return yaml.dump(DictionaryEncoder.auto_encode_to_dictionary(object_to_serialize))

    def dump(self, object_to_serialize, file_name: str) -> None:
        file = open(file_name, 'w')
        file.write(self.dumps(object_to_serialize))
        file.close()

    def loads(self, source: str):
        return DictionaryDecoder.auto_decode_to_object(yaml.safe_load(source))

    def load(self, file_name: str):
        file = open(file_name, 'r')
        source: str = file.read()
        file.close()

        return self.loads(source)

from library.iserializer import ISerializer
from library.formats.json.serialization.serialize import JsonSerializer


class Json(ISerializer):
    def dumps(self, object_to_serialize) -> str:
        return JsonSerializer.auto_serialize(object_to_serialize)

    def dump(self, object_to_serialize, file_name: str) -> None:
        file = open(file_name, 'w')

        file.write(JsonSerializer.auto_serialize(object_to_serialize))

        file.close()

    def load(self, file_name: str):
        pass

    def loads(self, source: str):
        pass

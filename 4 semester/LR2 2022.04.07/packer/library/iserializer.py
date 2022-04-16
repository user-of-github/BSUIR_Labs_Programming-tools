class ISerializer:
    def dump(self, object_to_serialize, file_name: str) -> None:
        pass

    def dumps(self, object_to_serialize) -> str:
        pass

    def load(self, file_name: str):
        pass

    def loads(self, source: str):
        pass

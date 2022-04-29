from abc import ABC, abstractmethod


class IPacker(ABC):
    @abstractmethod
    def dump(self, object_to_serialize, file_name: str) -> None:
        pass

    @abstractmethod
    def dumps(self, object_to_serialize) -> str:
        pass

    @abstractmethod
    def load(self, file_name: str):
        pass

    @abstractmethod
    def loads(self, source: str):
        pass

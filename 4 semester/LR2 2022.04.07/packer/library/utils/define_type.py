import inspect
import types


class DefineType:
    @staticmethod
    def is_primitive(to_check) -> bool:
        if isinstance(to_check, (int, float, str, bool)):
            return True
        elif to_check is None:
            return True
        else:
            return False

    @staticmethod
    def is_list_or_tuple(to_check) -> bool:
        return isinstance(to_check, list) or isinstance(to_check, tuple)

    @staticmethod
    def is_dict(to_check) -> bool:
        return isinstance(to_check, dict)

    @staticmethod
    def is_function(to_check) -> bool:
        return inspect.isroutine(to_check)

    @staticmethod
    def is_bytes(to_check) -> bool:
        return isinstance(to_check, (bytes, bytearray))

    @staticmethod
    def is_cell(to_check) -> bool:
        return isinstance(to_check, types.CellType)

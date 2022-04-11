from typing import Union


def serialize_basic_primitive(to_serialize: Union[int, float, str, bool]) -> str:
    if isinstance(to_serialize, str):
        return f'"{to_serialize}"'
    else:
        return f'{to_serialize}'
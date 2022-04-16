from typing import Union

from library.utils import constants


def serialize_basic_primitive(to_serialize: Union[int, float, str, bool]) -> str:
    if isinstance(to_serialize, str):
        return f'"{to_serialize}"'
    else:
        return f'{to_serialize}'


def serialize_none(none: None) -> str:
    return (
            '{'
            + f'type:{constants.NONE_DESIGNATION},'
            + f'value:{none}'
            + '}'
    )

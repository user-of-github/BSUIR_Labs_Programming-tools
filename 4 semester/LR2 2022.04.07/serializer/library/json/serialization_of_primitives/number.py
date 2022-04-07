from typing import Union
from library.json.serialization_of_primitives.type_designations import NUMBER


def serialize_number(number: Union[int, float]) -> str:
    return (
        '{'
        f'type:{NUMBER}'
        ','
        f'value:{number}'
        '}'
    )

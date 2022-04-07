from library.json.serialization_of_primitives.type_designations import BOOLEAN


def serialize_boolean(value: bool) -> str:
    return (
        '{'
        f'type:{BOOLEAN}'
        ','
        f'value:{value}'
        '}'
    )

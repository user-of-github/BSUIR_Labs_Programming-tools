from library.json.serialization_of_primitives.type_designations import STRING


def serialize_string(string: str) -> str:
    return (
        '{'
        f'type:{STRING}'
        ','
        f'value:"{string}"'
        '}'
    )
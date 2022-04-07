from library.json.serialization_of_primitives.auto_serialize_primitive import auto_serialize_primitive


def serialize_list(array: list) -> str:
    array_of_serialized_values: list = list()

    for item in array:
        array_of_serialized_values.append(auto_serialize_primitive(item))

    return (
            '[' +
            ','.join(array_of_serialized_values) +
            ']'
    )

from library.json.serialization_of_primitives.number import serialize_number
from library.json.serialization_of_primitives.string import serialize_string
from library.json.serialization_of_primitives.boolean import serialize_boolean
from library.json.serialization_of_primitives.list import serialize_list


def auto_serialize_primitive(object_to_serialize) -> str:
    if isinstance(object_to_serialize, int) or isinstance(object_to_serialize, float):
        return serialize_number(object_to_serialize)

    if isinstance(object_to_serialize, str):
        return serialize_string(object_to_serialize)

    if isinstance(object_to_serialize, bool):
        return serialize_boolean(object_to_serialize)

    if isinstance(object_to_serialize, list):
        return serialize_list(object_to_serialize)
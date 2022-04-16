import inspect


def is_primitive(to_check) -> bool:
    if isinstance(to_check, int):
        return True
    elif isinstance(to_check, float):
        return True
    elif isinstance(to_check, str):
        return True
    elif isinstance(to_check, bool):
        return True
    else:
        return False


def is_none(to_check) -> bool:
    return to_check is None


def is_list(to_check) -> bool:
    return isinstance(to_check, list)


def is_dict(to_check) -> bool:
    return isinstance(to_check, dict)


def is_function(to_check) -> bool:
    return inspect.isroutine(to_check)

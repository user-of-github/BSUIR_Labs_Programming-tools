ATTRIBUTES_OF_FUNCTION: list[str] = ['__name__', '__code__', '__defaults__', '__closure__']

ATTRIBUTES_OF_CODE_ATTRIBUTE = [
    'co_argcount',
    'co_posonlyargcount',
    'co_kwonlyargcount',
    'co_nlocals',
    'co_stacksize',
    'co_flags',
    'co_code',
    'co_consts',
    'co_names',
    'co_varnames',
    'co_filename',
    'co_name',
    'co_firstlineno',
    'co_lnotab',
    'co_freevars',
    'co_cellvars'
]

FUNCTION_DESIGNATION: str = 'function'
CLASS_DESIGNATION: str = 'class'

LIST_DESIGNATION: str = 'list'
TUPLE_DESIGNATION: str = 'tuple'
DICTIONARY_DESIGNATION: str = 'dict'

INT_DESIGNATION: str = 'int'
FLOAT_DESIGNATION: str = 'float'
BOOL_DESIGNATION: str = 'bool'
NONE_DESIGNATION: str = 'None'
STR_DESIGNATION: str = 'str'

INT_DESIGNATION: str = 'int'
FLOAT_DESIGNATION: str = 'float'
BOOL_DESIGNATION: str = 'bool'
NONE_DESIGNATION: str = 'none'
STR_DESIGNATION: str = 'str'

FUNCTION_DESIGNATION: str = 'function'
CLASS_DESIGNATION: str = 'class'

LIST_DESIGNATION: str = 'list'
TUPLE_DESIGNATION: str = 'tuple'
DICTIONARY_DESIGNATION: str = 'dict'
BYTES_DESIGNATION: str = 'bytes'

CELL_DESIGNATION: str = 'cell'
CODE_DESIGNATION: str = 'code'

ATTRIBUTES_OF_FUNCTION: list[str] = ['__name__', '__code__', '__defaults__', '__closure__']

ATTRIBUTES_OF_CODE_ATTRIBUTE: list[str] = [
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


SYMBOLS_TO_REPLACE_SPACE_IN_STRINGS: str = '#&$'

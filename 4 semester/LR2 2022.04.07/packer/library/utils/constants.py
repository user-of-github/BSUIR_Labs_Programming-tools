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

ATTRIBUTES_OF_CODE_TYPE: list[str] = [
    'co_argcount', 'co_posonlyargcount',
    'co_kwonlyargcount', 'co_nlocals',
    'co_stacksize', 'co_flags',
    'co_code', 'co_consts',
    'co_names', 'co_varnames',
    'co_filename', 'co_name',
    'co_firstlineno', 'co_lnotab',
    'co_freevars', 'co_cellvars'
]

SYMBOLS_TO_REPLACE_SPACE_IN_STRINGS: str = '#&$%'

UNNECESSARY_CLASS_ATTRIBUTES: list[str] = [
    '__annotations__', '__class__', '__delattr__', '__dict__', '__dir__',
    '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
    '__init_subclass__', '__le__', '__lt__',
    '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
    '__repr__', '__setattr__', '__sizeof__', '__subclasshook__',
    '__weakref__', '__hash__'
]


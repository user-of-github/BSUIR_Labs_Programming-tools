import os.path
import sys


def read_text_from_file(file_name: str) -> str:
    file = open(file_name, 'r')
    response = ''
    for line in file:
        response += line
    file.close()
    return response


# arguments should be passed in the following order: N, K (for example, pyhton3 analyzer.py 10 4)
def get_command_line_args(*default_values: tuple) -> (int, int):
    argv = sys.argv[1:]
    if len(argv) >= 2:
        return int(argv[0]), int(argv[1])
    elif len(argv) == 1:
        return int(argv[0]), default_values[1]
    else:
        return default_values[0], default_values[1]


def write_to_file(file_name: str, data: str) -> None:
    if not os.path.isfile(file_name):
        open(file_name, 'x')
    file = open(file_name, 'w')
    file.write(data)
    file.close()

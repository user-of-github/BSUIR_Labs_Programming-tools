import os.path


def read_text_from_file(file_name: str) -> str:
    file = open(file_name, 'r')
    response = ''
    for line in file:
        response += line
    file.close()
    return response


# аргументы подаются в порядке N, K (например, pyhton3 main.py 10 4)
def get_command_line_args(argv: list, *default_values: tuple) -> (int, int):
    if len(argv) >= 2:
        return int(argv[0]), int(argv[1])
    elif len(argv) == 1:
        return int(argv[0]), default_values[0]
    else:
        return default_values[0], default_values[1]


def write_to_file(file_name: str, data: str) -> None:
    if not os.path.isfile(file_name):
        open(file_name, 'x')
    file = open(file_name, 'w')
    file.write(data)
    file.close()

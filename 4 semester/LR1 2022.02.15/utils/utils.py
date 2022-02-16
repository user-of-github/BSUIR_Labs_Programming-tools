from data.data import DEFAULT_N, DEFAULT_K


def read_text_from_file(file_name: str) -> str:
    file = open(file_name, 'r')
    response = ''
    for line in file:
        response += line
    return response


# аргументы подаются в порядке N, K (например, pyhton3 main.py 10 4)
def get_command_line_args(argv: list) -> (int, int):
    if len(argv) >= 2:
        return argv[0], argv[1]
    elif len(argv) == 1:
        return argv[0], DEFAULT_K
    else:
        return DEFAULT_N, DEFAULT_K

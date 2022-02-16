def read_text_from_file(file_name: str) -> str:
    file = open(file_name, 'r')
    response = ''
    for line in file:
        response += line
    return response

from utils.utils import read_text_from_file, get_command_line_args, write_to_file
from data.data import DEFAULT_N, DEFAULT_K
from data.data import SOURCE_FILE, OUTPUT_FILE
from text_analyzer.types import QueryStructure
from text_analyzer.text_analyzer import analyze_text


def main() -> None:
    command_line_arguments = get_command_line_args(DEFAULT_N, DEFAULT_K)
    query = QueryStructure(*command_line_arguments)
    data = read_text_from_file(SOURCE_FILE)

    response = analyze_text(data, query)
    write_to_file(OUTPUT_FILE, str(response))


if __name__ == '__main__':
    main()
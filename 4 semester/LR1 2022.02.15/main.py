import sys

from utils.utils import read_text_from_file, get_command_line_args
from data.data import SOURCE_FILE
from text_analyzer.text_analyzer import analyze_text, QueryStructure


def main() -> None:
    query = QueryStructure(*get_command_line_args(sys.argv))
    data = read_text_from_file(SOURCE_FILE)

    response = analyze_text(data, query)
    
    print(response)


if __name__ == '__main__':
    main()

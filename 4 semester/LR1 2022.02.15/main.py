from utils.utils import read_text_from_file
from data.data import SOURCE_FILE
from text_analyzer.text_analyzer import analyze_text


def main() -> None:
    input_text = read_text_from_file(SOURCE_FILE)

    response = analyze_text(input_text)

    print(response)


if __name__ == '__main__':
    main()

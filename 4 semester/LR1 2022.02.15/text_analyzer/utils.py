def filter_empty_words(words: list) -> list:
    def check_if_doesnt_consist_of_whitespaces(word: str) -> bool:
        if word == '':
            return False
        elif word == '\t':
            return False
        elif word == '\n':
            return False
        elif word == '.':
            return False
        elif word == '?':
            return False
        elif word == ',':
            return False
        else:
            return True

    return list(filter(check_if_doesnt_consist_of_whitespaces, words))


def convert_to_same_case(words: list) -> None:
    for counter in range(0, len(words)):
        words[counter] = words[counter].lower()


def get_frequencies_of_words(words: list) -> dict:
    response = {}

    for word in words:
        response[word] = 1 if response.get(word) is None else response[word] + 1

    return response


def get_average_and_median_words_number_in_sentence(text: str) -> (int, int):
    words = text.split('.')


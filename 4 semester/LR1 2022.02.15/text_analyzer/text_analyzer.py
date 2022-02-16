import re

from text_analyzer.utils import filter_empty_words
from text_analyzer.utils import get_frequencies_of_words
from text_analyzer.utils import convert_to_same_case
import text_analyzer.defaults


class QueryStructure:  # object with parameters to pass to my function
    def __init__(self, n: int = 10, k: int = 4):
        self.n = 10
        self.k = 4


class ResponseStructure:  # structure of response of my function
    def __init__(self, words_count: int, words_frequency: dict):
        self.words_count = words_count
        self.words_frequency = words_frequency

    def __str__(self) -> str:
        return f'Words count: {self.words_count}\n' \
               f'Words frequency: {self.words_frequency}\n' \
               f'Other information...\n'


def analyze_text(text: str, query: QueryStructure = QueryStructure()) -> ResponseStructure:
    words = filter_empty_words(re.split(text_analyzer.defaults.SPLIT_WORDS_BY, text))

    convert_to_same_case(words)

    words_frequency = get_frequencies_of_words(words)

    # average_sentence_words, median_sentence_words = 5, 6

    # print(words)

    return ResponseStructure(
        len(words),
        words_frequency
    )

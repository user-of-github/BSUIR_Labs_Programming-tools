import dataclasses


# object with parameters to pass to function
@dataclasses.dataclass
class Query:
    text: str
    anagram_length: int
    number_of_most_frequent: int


# structure of response of function
class Response:
    def __init__(self,
                 words_count: int, words_frequency: dict,
                 sentences_count: int, words_average: float,
                 words_median: float, frequent_k_grams: dict):
        self.words_count = words_count
        self.words_frequency = words_frequency
        self.sentences_count = sentences_count
        self.words_average_count = words_average
        self.words_median_count = words_median
        self.frequent_k_grams = frequent_k_grams

    def __str__(self) -> str:
        return (
            f'Text analyzer response:\n'
            f'\tWords count: {self.words_count}\n'
            f'\tWords frequency: {self.words_frequency}\n'
            f'\tSentences count: {self.sentences_count}\n'
            f'\tAverage number of words in sentences: {self.words_average_count}\n'
            f'\tMedian number of words in sentences: {self.words_median_count}\n'
            f'\tThe most frequent N-grams (K pieces): {self.frequent_k_grams}'
        )

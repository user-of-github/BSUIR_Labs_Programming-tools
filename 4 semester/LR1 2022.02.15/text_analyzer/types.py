# object with parameters to pass to function
class Query:
    def __init__(self, text: str, n: int, k: int):
        self.text = text
        self.anagram_length = n
        self.number_of_most_frequent = k

    def __str__(self) -> str:
        return (
            f'Anagrams\' length: {self.anagram_length}. '
            f'How many of most frequent to print: {self.number_of_most_frequent}'
        )


# structure of response of function
class Response:
    def __init__(self,
                 words_count: int, words_frequency: dict,
                 sentences_count: int, words_average: float,
                 words_median: int, frequent_k_grams: dict):
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

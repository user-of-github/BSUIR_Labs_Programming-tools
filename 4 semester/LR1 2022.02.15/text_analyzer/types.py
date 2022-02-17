from data.data import DEFAULT_N, DEFAULT_K


class QueryStructure:  # object with parameters to pass to my function
    def __init__(self, n: int = DEFAULT_N, k: int = DEFAULT_K):
        self.n = n
        self.k = k

    def __str__(self):
        return f'N = {self.n}, K = {self.k}'


class ResponseStructure:  # structure of response of my function
    def __init__(self,
                 words_count: int, words_frequency: dict,
                 sentences_count: int, words_average: float,
                 words_median: int):
        self.words_count = words_count
        self.words_frequency = words_frequency
        self.sentences_count = sentences_count
        self.words_average_count = words_average
        self.words_median_count = words_median

    def __str__(self) -> str:
        return f'Text analyze response:\n' \
               f'\tWords count: {self.words_count}\n' \
               f'\tWords frequency: {self.words_frequency}\n' \
               f'\tSentences count: {self.sentences_count}\n' \
               f'\tAverage number of words in sentences: {self.words_average_count}\n' \
               f'\tMedian number of words in sentences: {self.words_median_count}\n'

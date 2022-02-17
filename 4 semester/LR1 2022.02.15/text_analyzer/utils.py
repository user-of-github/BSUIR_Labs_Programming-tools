import re
from collections import OrderedDict
from text_analyzer.defaults import SPLIT_WORDS_BY, NOT_PART_OF_THE_WORD, SPLIT_SENTENCES_BY


def filter_invalid_words(words: list) -> list:
    def check_if_doesnt_consist_of_whitespaces(word: str) -> bool:
        for sign in NOT_PART_OF_THE_WORD:
            if word == sign:
                return False
        return True

    return list(filter(check_if_doesnt_consist_of_whitespaces, words))


def get_separate_words(text: str) -> list:
    return filter_invalid_words(re.split(SPLIT_WORDS_BY, text))


def get_frequencies_of_words(words: list) -> dict:
    response = dict()

    for word in words:
        response[word] = 1 if response.get(word) is None else response[word] + 1

    response = sorted(response.items(), key=lambda kv: (kv[1], kv[0]))
    response.reverse()

    return dict(response)


def filter_invalid_sentences(raw_sentences: list) -> list:
    check_if_isnt_empty = lambda sentence: len(get_separate_words(sentence)) != 0

    return list(filter(check_if_isnt_empty, raw_sentences))


def get_separate_sentences(text: str) -> list:
    return filter_invalid_sentences(re.split(SPLIT_SENTENCES_BY, text))


def get_sentences_words_counts(sentences: list) -> list:
    response = list()
    for sentence in sentences:
        response.append(len(get_separate_words(sentence)))

    return response


def get_average_sentence_words_count(sentences_words_count: list) -> float:
    return sum(sentences_words_count) / len(sentences_words_count)


def get_median_sentence_words_count(sentences_words_count: list) -> int:
    query_copy = sentences_words_count.copy()
    query_copy.sort()
    return query_copy[len(sentences_words_count) // 2]

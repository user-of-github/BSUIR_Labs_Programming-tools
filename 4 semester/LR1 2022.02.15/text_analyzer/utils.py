import re
import operator
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

    return dict(sorted(response.items(), key=operator.itemgetter(1), reverse=True))


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


def get_k_grams_for_word(word: str, length: int) -> list:
    response = list()
    for counter in range(0, len(word) - length + 1):
        response.append(word[counter:counter+length])
    return response


def get_k_grams_counts(words: list, k: int) -> dict:
    response = dict()
    for word in words:
        word_k_grams = get_k_grams_for_word(word, k)
        for gram in word_k_grams:
            response[gram] = 1 if response.get(gram) is None else response[gram] + 1

    return response


def get_most_frequent_k_grams(k_grams_counts: dict, n: int) -> dict:
    return dict(sorted(k_grams_counts.items(), key=operator.itemgetter(1), reverse=True)[0:n])

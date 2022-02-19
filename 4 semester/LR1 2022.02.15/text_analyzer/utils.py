import re
import operator
from text_analyzer.constants import SPLIT_WORDS_BY, NOT_WORD, SENTENCE


def filter_invalid_words(words: list) -> list:
    return list(filter(lambda word: re.match(NOT_WORD, word) is None and word != '', words))


def get_separate_words(text: str) -> list:
    return filter_invalid_words(re.split(SPLIT_WORDS_BY, text))


def get_frequencies_of_words(words: list) -> dict:
    response = dict()

    for word in words:
        if response.get(word) is None:
            response[word] = 1
        else:
            response[word] += 1

    return dict(sorted(response.items(), key=operator.itemgetter(1), reverse=True))


def filter_invalid_sentences(raw_sentences: list) -> list:
    return list(filter(lambda sentence: len(get_separate_words(sentence)) != 0, raw_sentences))


def get_separate_sentences(text: str) -> list:
    return re.findall(SENTENCE, text)


def get_words_in_sentences(sentences: list) -> list:
    response = list()

    for sentence in sentences:
        response.append(get_separate_words(sentence.lower()))

    return response


def get_sentences_words_counts(words_in_sentences: list) -> list:
    response = list()

    for sentence in words_in_sentences:
        response.append(len(sentence))

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
        response.append(word[counter:counter + length])

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

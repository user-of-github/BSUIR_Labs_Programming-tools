from text_analyzer.types import Query, Response
from text_analyzer.utils import get_frequencies_of_words
from text_analyzer.utils import get_separate_sentences
from text_analyzer.utils import get_sentences_words_counts
from text_analyzer.utils import get_average_sentence_words_count
from text_analyzer.utils import get_median_sentence_words_count
from text_analyzer.utils import get_words_in_sentences
from text_analyzer.utils import get_k_grams_counts
from text_analyzer.utils import get_most_frequent_k_grams


def analyze_text(query: Query) -> Response:
    sentences = get_separate_sentences(query.text)

    words_in_sentences = get_words_in_sentences(sentences)
    all_words = sum(words_in_sentences, list())
    words_frequencies = get_frequencies_of_words(all_words)

    words_in_sentences_counts = get_sentences_words_counts(words_in_sentences)
    average_sentence_words = get_average_sentence_words_count(words_in_sentences_counts)
    median_sentence_words = get_median_sentence_words_count(words_in_sentences_counts)

    all_k_grams = get_k_grams_counts(all_words, query.anagram_length)
    most_frequent_k_grams = get_most_frequent_k_grams(all_k_grams, query.number_of_most_frequent)

    return Response(
        words_count=len(all_words),
        words_frequency=words_frequencies,
        sentences_count=len(sentences),
        words_average=average_sentence_words,
        words_median=median_sentence_words,
        frequent_k_grams=most_frequent_k_grams
    )

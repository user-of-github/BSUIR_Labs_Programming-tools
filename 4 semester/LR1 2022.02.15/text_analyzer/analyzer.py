from text_analyzer.utils import get_separate_words
from text_analyzer.utils import get_frequencies_of_words
from text_analyzer.utils import get_separate_sentences
from text_analyzer.utils import get_sentences_words_counts
from text_analyzer.utils import get_average_sentence_words_count
from text_analyzer.utils import get_median_sentence_words_count
from text_analyzer.types import Query, Response
from text_analyzer.utils import get_k_grams_counts
from text_analyzer.utils import get_most_frequent_k_grams


def analyze_text(source: str, query: Query = Query()) -> Response:
    text = source.lower()

    words = get_separate_words(text)
    words_frequency = get_frequencies_of_words(words)

    sentences = get_separate_sentences(text)
    words_in_sentences_counts = get_sentences_words_counts(sentences)
    average_words_count = get_average_sentence_words_count(words_in_sentences_counts)
    median_words_count = get_median_sentence_words_count(words_in_sentences_counts)

    k_grams_counts = get_k_grams_counts(words, query.anagram_length)  # all
    most_frequent_k_grams = get_most_frequent_k_grams(k_grams_counts, query.number_of_most_frequent)  # only first N needed

    return Response(
        words_count=len(words),
        words_frequency=words_frequency,
        sentences_count=len(sentences),
        words_average=average_words_count,
        words_median=median_words_count,
        frequent_k_grams=most_frequent_k_grams
    )

SPLIT_WORDS_BY: str = (
    r'\;|'
    r'\,|'
    r'\.|'
    r'\:|'
    r'\!|'
    r'\?|'
    r'\(|'
    r'\)|'
    r'\ |'
    r'\"|'
    r'\'|'
    r'\n|'
    r'\—|'
    r'\«|'
    r'\»'
)

NOT_WORD: str = r'[0-9\)\(\"\@\,\.\ \«\»\-\—\;\:]+'

SENTENCE: str = (
    r'[А-ЯA-ZЁ0-9]'  # first Capital letter
    r'(?:'
    r'(?:[a-zа-яё0-9\,\-\ \\.\:\\"\\n]*)'  # any sequence (including big letters) without dot
    r'|'
    r'(?:[A-Za-zА-Яа-яё0-9\,\-\:\\"\ \\n]*)'  # any sequence of small letters WITH a dot (etc.)
    r')'
    r'[?!.]+'
)
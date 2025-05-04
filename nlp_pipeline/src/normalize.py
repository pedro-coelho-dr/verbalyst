import unicodedata

def normalize_word(word: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize("NFKD", word)
        if not unicodedata.combining(c)
    ).lower()

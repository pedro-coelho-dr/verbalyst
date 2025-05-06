import unicodedata

def normalize_word(word: str) -> str:
    """Remove acentos, espaços e normaliza para minúsculas."""
    return ''.join(
        c for c in unicodedata.normalize('NFKD', word.lower().strip())
        if not unicodedata.combining(c)
    )

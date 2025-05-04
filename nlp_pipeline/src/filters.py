from normalize import normalize_word

def load_word_set(path: str) -> set[str]:
    with open(path, "r", encoding="utf-8") as f:
        return {line.strip().lower() for line in f if line.strip()}

def filter_by_dict(words: list[str], dict_path: str) -> list[str]:
    allowed = load_word_set(dict_path)
    return [w for w in words if w in allowed]

def remove_duplicates_normalized(words: list[str]) -> list[str]:
    seen = set()
    result = []
    for w in words:
        norm = normalize_word(w)
        if norm not in seen:
            seen.add(norm)
            result.append(norm)
    return result

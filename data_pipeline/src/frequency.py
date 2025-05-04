def extract_top_words(freq_path: str, top_n: int = 10000, min_len: int = 2) -> list[str]:
    words = []
    with open(freq_path, "r", encoding="latin-1") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) < 2:
                continue
            word = parts[1]
            if len(word) >= min_len and word.isalpha():
                words.append(word.lower())
            if len(words) >= top_n:
                break
    return words

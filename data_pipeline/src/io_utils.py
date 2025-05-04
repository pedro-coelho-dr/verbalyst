def save_log(words: list[str], path: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(sorted(words)))

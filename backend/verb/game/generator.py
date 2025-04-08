import json
from pathlib import Path
from verb.core.model import load_model
from verb.core.config import GAMES_PATH


def normalize_score(similarity: float, min_similarity: float, max_similarity: float) -> float:
    if max_similarity == min_similarity:
        return 0.0
    return round((similarity - min_similarity) / (max_similarity - min_similarity) * 99.99, 2)


def generate_game(target_word: str, game_id: int) -> None:
    model = load_model()

    if target_word not in model:
        raise ValueError(f"The word '{target_word}' is not present in the model vocabulary.")

    similar_words = model.most_similar(target_word, topn=len(model.key_to_index))
    similarities = [score for _, score in similar_words]
    max_similarity = max(similarities)
    min_similarity = min(similarities)

    ranking = {
        word: normalize_score(score, min_similarity, max_similarity)
        for word, score in similar_words
    }

    Path(GAMES_PATH).mkdir(parents=True, exist_ok=True)
    output_path = GAMES_PATH / f"{game_id}.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({
            "target_word": target_word,
            "ranking": ranking
        }, f, ensure_ascii=False, indent=2)

    print(f"Game saved to: {output_path}")


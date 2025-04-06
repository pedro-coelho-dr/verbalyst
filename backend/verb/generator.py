import json
from verb.model import load_model
from verb.config import GAMES_PATH
from pathlib import Path

def normalize_score(similarity: float, min_similarity: float, max_similarity: float) -> int:
    return round((similarity - min_similarity) / (max_similarity - min_similarity) * 100)

def generate_game(target_word: str, output_filename: str) -> None:
    model = load_model()

    if target_word not in model:
        raise ValueError(f"The word '{target_word}' is not present in the model vocabulary.")

    # Get similarity scores to all other words
    similar_words = model.most_similar(target_word, topn=len(model.key_to_index))

    # Extract min and max similarity values for normalization
    similarities = [score for _, score in similar_words]
    max_similarity = max(similarities)
    min_similarity = min(similarities)

    # Build a normalized ranking dictionary
    ranking = {
        word: normalize_score(score, min_similarity, max_similarity)
        for word, score in similar_words
    }

    # Ensure output directory exists
    Path(GAMES_PATH).mkdir(parents=True, exist_ok=True)
    output_path = GAMES_PATH / output_filename

    # Save to JSON file
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({
            "target_word": target_word,
            "ranking": ranking
        }, f, ensure_ascii=False, indent=2)

    print(f"Game saved to: {output_path}")

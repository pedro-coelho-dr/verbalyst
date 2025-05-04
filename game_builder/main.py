from config import MODEL_PATH, OUTPUT_DIR, TARGETS_PATH, NUM_HINTS
from src.target import load_targets
from src.rank import get_word_scores
from src.coordinates import get_relative_coordinates_mds
from src.hint import get_filtered_hints
from src.build import build_game_dict
from src.export import save_game_json
from gensim.models import KeyedVectors

def load_model(path: str) -> KeyedVectors:
    return KeyedVectors.load(path, mmap='r')

def main():
    model = load_model(MODEL_PATH)
    vocab = list(model.key_to_index.keys())
    targets = load_targets(TARGETS_PATH)

    for target in targets:
        if target not in vocab:
            print(f"[IGNORED] '{target}'")
            continue
        # Ranks

        scores = get_word_scores(target, vocab, model)
        hints = get_filtered_hints(target, vocab, model, scores, NUM_HINTS)

        # Coordenadas
        coords = get_relative_coordinates_mds(target, hints, model)
        target_coords = {"x": 0.0, "y": 0.0}
        hint_data = [
            {"word": word, "x": coords[word][0], "y": coords[word][1]}
            for word in hints
        ]

        # Hints

        game = build_game_dict(target, target_coords, hint_data)
        save_game_json(game, OUTPUT_DIR)

if __name__ == "__main__":
    main()

from config import MODEL_PATH, OUTPUT_DIR, TARGETS_PATH, NUM_HINTS
from src import load_targets, get_distances, get_coordinates, get_hints, save_game
from gensim.models import KeyedVectors


def load_model(path: str) -> KeyedVectors:
    print(f"[INFO] Loading model from: {path}")
    return KeyedVectors.load(path, mmap="r")


def build_game(target: str, vocab: list[str], model, output_dir: str, num_hints: int) -> None:
    print(f"\n[BUILD] Starting game build for target: '{target}'")

    if target not in vocab:
        print(f"[IGNORED] '{target}' not found in model vocabulary.")
        return

    print("  → Calculating distances...")
    distances = get_distances(target, vocab, model)
    distances = [entry for entry in distances if entry[0] != target]
    distances_dict = dict(distances)

    print(f"  → Found {len(distances)} candidate words.")

    print("  → Selecting hints...")
    hints = get_hints(target, vocab, model, distances, num_hints)

    print(f"  → {len(hints)} hints selected.")

    print("  → Computing coordinates...")
    coords = get_coordinates(target, list(distances_dict.keys()), model)

    # Monta dados dos hints
    hint_data = [
        {
            "word": word,
            "x": coords[word][0],
            "y": coords[word][1],
            "distance": distances_dict[word]
        }
        for word in hints
    ]

    # Monta dados de todas as palavras
    words_data = [
        {
            "word": word,
            "x": coords[word][0],
            "y": coords[word][1],
            "distance": distances_dict[word]
        }
        for word in distances_dict
    ]

    # JSON final
    game = {
        "target_word": target,
        "hints": hint_data,
        "words": words_data
    }

    save_game(game, output_dir)
    print(f"[OK] Game saved for '{target}'")


def main():
    print("[INIT] Starting game generation...")
    model = load_model(MODEL_PATH)
    vocab = list(model.key_to_index.keys())
    targets = load_targets(TARGETS_PATH)

    print(f"[INFO] Loaded {len(vocab)} words from model.")
    print(f"[INFO] Loaded {len(targets)} target words.")

    for idx, target in enumerate(targets, 1):
        print(f"\n=== Building {idx}/{len(targets)} ===")
        build_game(target, vocab, model, OUTPUT_DIR, NUM_HINTS)

    print("\n[DONE] All games built successfully.")


if __name__ == "__main__":
    main()

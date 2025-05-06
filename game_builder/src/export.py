import json
import os
import re
from pathlib import Path

def get_next_game_id(output_dir: str) -> int:
    os.makedirs(output_dir, exist_ok=True)

    existing_files = [
        f for f in os.listdir(output_dir)
        if f.endswith(".json") and re.fullmatch(r"\d{4}\.json", f)
    ]

    ids = [int(f[:-5]) for f in existing_files]
    return max(ids) + 1 if ids else 1

def save_game(game_data: dict, output_dir: str) -> None:
    game_id = get_next_game_id(output_dir)
    filename = f"{game_id:04}.json"
    file_path = os.path.join(output_dir, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(game_data, f, ensure_ascii=False, indent=2)

def get_next_vocab_filename(output_dir: str, prefix: str = "vocab", ext: str = ".txt") -> str:
    vocab_dir = Path(output_dir) / "vocab"
    vocab_dir.mkdir(parents=True, exist_ok=True)

    existing_files = [
        f.name for f in vocab_dir.glob(f"{prefix}[0-9][0-9]*{ext}")
    ]

    existing_ids = [
        int(re.search(rf"{prefix}(\d+){ext}", name).group(1))
        for name in existing_files if re.search(rf"{prefix}(\d+){ext}", name)
    ]

    next_id = max(existing_ids) + 1 if existing_ids else 1
    return f"{prefix}{next_id:02}{ext}"

def save_vocab(vocab: list[str], output_dir: str) -> None:
    filename = get_next_vocab_filename(output_dir)
    output_path = Path(output_dir) / "vocab" / filename

    with open(output_path, "w", encoding="utf-8") as f:
        for word in vocab:
            f.write(f"{word}\n")

    print(f"[INFO] Saved vocab to: {output_path}")


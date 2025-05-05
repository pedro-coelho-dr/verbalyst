import json
import os
import re

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
import json
from app.core.database import get_session
from app.models import Game
from app.core.config import settings

def populate_static_games() -> None:
    with get_session() as session:
        for json_file in sorted(settings.STATIC_GAMES_DIR.glob("*.json")):
            game_id = int(json_file.stem)
            if session.get(Game, game_id):
                print(f"[SKIP] Game {game_id} already exists.")
                continue

            with open(json_file, encoding="utf-8") as f:
                data = json.load(f)

            game = Game(
                id=game_id,
                target_word=data["target_word"],
                hints=data["hints"],
                coordinates=data["coordinates"],
                rank=data["rank"],
            )
            session.add(game)
            print(f"[ADD] Game {game_id} added.")

        session.commit()
        print("[DONE] All games inserted.")

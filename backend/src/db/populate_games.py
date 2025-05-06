import json
from pathlib import Path

from sqlmodel import select

from core import settings, get_session
from models import Word, Game, Hint, Distance



def get_or_create_word(session, word_str: str) -> Word:
    word = session.exec(select(Word).where(Word.word == word_str)).first()
    if word is None:
        word = Word(word=word_str)
        session.add(word)
        session.commit()
        session.refresh(word)
    return word


def populate_from_json(json_path: Path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    with get_session() as session:
        # Palavra-alvo
        target = get_or_create_word(session, data["target_word"])

        # Verifica se já existe jogo para essa palavra
        existing_game = session.exec(
            select(Game).where(Game.fk_target_word == target.id)
        ).first()

        if existing_game:
            print(f"[SKIP] Game for '{target.word}' already exists.")
            return

        # Criar novo jogo
        game = Game(fk_target_word=target.id)
        session.add(game)
        session.commit()
        session.refresh(game)

        # Dicas
        for hint_data in data["hints"]:
            hint_word = get_or_create_word(session, hint_data["word"])
            hint = Hint(
                fk_target=target.id,
                fk_word=hint_word.id,
                distance=hint_data["distance"],
                x=hint_data["x"],
                y=hint_data["y"]
            )
            session.add(hint)

        # Distâncias
        for word_data in data["words"]:
            word = get_or_create_word(session, word_data["word"])
            distance = Distance(
                fk_target=target.id,
                fk_word=word.id,
                distance=word_data["distance"],
                x=word_data["x"],
                y=word_data["y"]
            )
            session.add(distance)

        session.commit()
        print(f"[OK] Game '{target.word}' loaded from {json_path.name}")



def main():
    folder = settings.STATIC_GAMES_DIR
    for json_file in sorted(folder.glob("*.json")):
        print(f"[LOAD] {json_file.name}")
        populate_from_json(json_file)


if __name__ == "__main__":
    main()

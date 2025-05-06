from core import settings, get_session

from models import Word



def load_vocab() -> list[str]:
    vocab_path = settings.STATIC_GAMES_DIR / "__vocab__.txt"
    with open(vocab_path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def populate_words():
    vocab = load_vocab()
    with get_session() as session:
        existing_words = {w.word for w in session.query(Word.word).all()}
        new_words = [Word(word=w) for w in vocab if w not in existing_words]

        if not new_words:
            print("[SKIP] No new words to insert.")
            return

        session.add_all(new_words)
        session.commit()
        print(f"[DONE] {len(new_words)} words inserted.")

if __name__ == "__main__":
    populate_words()

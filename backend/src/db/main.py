from db import create_db_and_tables, populate_words, populate_games


def run_all():
    print("[STEP 1] Creating DB schema...")
    create_db_and_tables()

    print("[STEP 2] Populating vocab words...")
    populate_words()

    print("[STEP 3] Populating games...")
    populate_games()

    print("[DONE] All steps completed successfully.")


if __name__ == "__main__":
    run_all()

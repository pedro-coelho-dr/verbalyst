import os
from sqlmodel import create_engine, Session

DATABASE_URL = os.getenv("DATABASE_URL")

# echo=True para dev, False para prod
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    return Session(engine)

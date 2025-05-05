from fastapi import FastAPI
from contextlib import asynccontextmanager
from backend.app.db.db import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()  # Inicializa o banco de dados
    yield  # Aqui o app roda
    # colocar código de teardown após o yield

app = FastAPI(lifespan=lifespan)

@app.get("/verb/")
def check_verb():
    return {"status": "verb ok"}

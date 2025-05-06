from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("[LIFESPAN] App starting...")
    yield
    print("[LIFESPAN] App shutting down...")

app = FastAPI(lifespan=lifespan)


@app.get("/verb/")
def check_verb():
    return {"status": "verb ok"}

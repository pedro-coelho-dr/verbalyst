from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.api import api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("[LIFESPAN] App starting...")
    yield
    print("[LIFESPAN] App shutting down...")

app = FastAPI(lifespan=lifespan)
app.include_router(api_router)

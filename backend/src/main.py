from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.api import api_router
from src.auth import auth_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("[LIFESPAN] App starting...")
    yield
    print("[LIFESPAN] App shutting down...")

app = FastAPI(
    title="Verbalyst API",
    version="0.1.0",
    description="API for the Verbalyst semantic word game",
    lifespan=lifespan,
    root_path="/verb",
    docs_url="/docs",
    redoc_url=None,
    openapi_url="/openapi.json"
)


app.include_router(api_router)
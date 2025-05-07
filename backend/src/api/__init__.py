from fastapi import APIRouter
from .guess import router as guess_router
from .hint import router as hint_router

api_router = APIRouter()

@api_router.get("/health")
def check_status():
    return {"status": "ok"}

api_router.include_router(guess_router, prefix="/guess", tags=["Guess"])
api_router.include_router(hint_router, prefix="/hint", tags=["Hint"])

__all__ = ["api_router"]

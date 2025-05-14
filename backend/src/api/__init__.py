from fastapi import APIRouter
from .guess import guess_router
from .hint import hint_router
from ..auth.oauth import oauth_router

api_router = APIRouter()
api_router.include_router(guess_router, prefix="/guess", tags=["Guess"])
api_router.include_router(hint_router, prefix="/hint", tags=["Hint"])
api_router.include_router(oauth_router, prefix="/auth", tags=["Auth"])

__all__ = ["api_router"]

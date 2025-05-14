from fastapi import APIRouter
from .daily import daily_router
from .room import room_router
from ..auth.oauth import oauth_router

api_router = APIRouter()
api_router.include_router(oauth_router, prefix="/auth", tags=["Auth"])
api_router.include_router(daily_router, prefix="/daily", tags=["Daily"])
api_router.include_router(room_router, prefix="/room", tags=["Room"])

__all__ = ["api_router"]

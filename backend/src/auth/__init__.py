from fastapi import APIRouter
from .oauth import oauth_router
from .jwt import create_access_token
from .dependencies import get_current_user
from .github import get_github_user, get_or_create_profile

auth_router = APIRouter()
auth_router.include_router(oauth_router)

__all__ = [
    "auth_router",
    "create_access_token",
    "get_current_user",
    "get_github_user",
    "get_or_create_profile"
]
from sqlmodel import Session, select
from src.models.profile import Profile
from src.core.config import settings
import httpx
from fastapi.security import OAuth2PasswordBearer

CLIENT_ID = settings.OAUTH_CLIENT_ID
CLIENT_SECRET = settings.OAUTH_CLIENT_SECRET
REDIRECT_URI = settings.OAUTH_REDIRECT_URI

async def get_github_user(code: str) -> dict:
    async with httpx.AsyncClient() as client:
        token_res = await client.post(
            "https://github.com/login/oauth/access_token",
            headers={"Accept": "application/json"},
            data={
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "code": code,
                "redirect_uri": REDIRECT_URI,
            },
        )
        if token_res.status_code != 200:
            raise ValueError("Failed to fetch access token")
        token = token_res.json().get("access_token")
        if not token:
            raise ValueError("No token returned")

        user_res = await client.get(
            "https://api.github.com/user",
            headers={"Authorization": f"token {token}"}
        )
        if user_res.status_code != 200:
            raise ValueError("Failed to fetch user data")
        return user_res.json()


def get_or_create_profile(user_data: dict, db: Session) -> Profile:
    github_id = str(user_data["id"])
    username = user_data["login"]

    stmt = select(Profile).where(Profile.auth_provider == "github", Profile.auth_sub == github_id)
    profile = db.exec(stmt).first()

    if not profile:
        profile = Profile(
            auth_provider="github",
            auth_sub=github_id,
            username=username
        )
        db.add(profile)
        db.commit()
        db.refresh(profile)

    return profile

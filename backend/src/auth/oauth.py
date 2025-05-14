from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from sqlmodel import Session
from src.auth.jwt import create_access_token
from src.auth.github import get_or_create_profile
from src.schemas.token import Token
from src.core.database import get_session
from src.core.config import settings
import httpx
import secrets

oauth_router = APIRouter(tags=["Auth"])

CLIENT_ID = settings.OAUTH_CLIENT_ID
CLIENT_SECRET = settings.OAUTH_CLIENT_SECRET
REDIRECT_URI = settings.OAUTH_REDIRECT_URI
IS_PROD = settings.APP_ENV == "prod"

if not all([CLIENT_ID, CLIENT_SECRET, REDIRECT_URI]):
    import warnings
    warnings.warn("GitHub OAuth will not function: OAUTH_* env vars not fully set.")

@oauth_router.get("/login")
def login():
    state = secrets.token_urlsafe(16)
    github_auth_url = (
        "https://github.com/login/oauth/authorize"
        f"?client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope=read:user"
        f"&state={state}"
    )
    response = RedirectResponse(github_auth_url)
    response.set_cookie(
        key="oauth_state",
        value=state,
        httponly=True,
        max_age=300,  # 5 minutes
        secure=IS_PROD,
        samesite="Lax"
    )
    return response

@oauth_router.get("/callback", response_model=Token)
async def callback(request: Request, code: str, state: str, db: Session = Depends(get_session)):
    saved_state = request.cookies.get("oauth_state")
    if not saved_state or saved_state != state:
        raise HTTPException(status_code=400, detail="Invalid OAuth state")

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
            return JSONResponse(status_code=token_res.status_code, content={"error": "Failed to fetch access token"})

        token_data = token_res.json()
        access_token = token_data.get("access_token")
        if not access_token:
            return JSONResponse(status_code=400, content={"error": "Access token not returned"})

        user_res = await client.get(
            "https://api.github.com/user",
            headers={"Authorization": f"token {access_token}"}
        )
        if user_res.status_code != 200:
            return JSONResponse(status_code=user_res.status_code, content={"error": "Failed to fetch user data"})

        user_data = user_res.json()

    profile = get_or_create_profile(user_data, db)
    jwt_token = create_access_token({"sub": str(profile.id)})

    return {"access_token": jwt_token, "token_type": "bearer"}

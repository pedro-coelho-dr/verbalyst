from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, AnyHttpUrl, field_validator
from pathlib import Path
from typing import List, Union, Optional


class Settings(BaseSettings):
    # Environment
    APP_ENV: str = "dev"
    # Database
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    DATABASE_URL: PostgresDsn

    # OAuth
    OAUTH_CLIENT_ID: str
    OAUTH_CLIENT_SECRET: str
    OAUTH_REDIRECT_URI: str

    # JWT
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 30

    # CORS
    CORS_ORIGINS: Union[str, List[AnyHttpUrl]] = ""

    # Paths
    STATIC_GAMES_DIR: Path = Path("/app/static_games")

    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def split_cors_origins(cls, v):
        if isinstance(v, str) and v:
            return [i.strip() for i in v.split(",") if i.strip()]
        return v or []

    class Config:
        case_sensitive = True


settings = Settings()

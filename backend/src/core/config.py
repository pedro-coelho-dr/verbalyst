from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, AnyHttpUrl, field_validator
from pathlib import Path
from typing import List, Union


class Settings(BaseSettings):
    # Database
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    DATABASE_URL: PostgresDsn

    # CORS
    CORS_ORIGINS: Union[str, List[AnyHttpUrl]] = ""

    # Paths
    STATIC_GAMES_DIR: Path = Path("/app/static_games")

    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def split_cors_origins(cls, v):
        if isinstance(v, str):
            return [i.strip() for i in v.split(",") if i.strip()]
        return v

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

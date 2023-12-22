from pydantic_settings import BaseSettings

from config import settings


class Settings(BaseSettings):
    db_url: str = f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}?async_fallback=True"
    db_cache_url: str = f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}"
    db_echo: bool = True


db_settings = Settings()

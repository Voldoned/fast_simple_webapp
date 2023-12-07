from pydantic_settings import BaseSettings

from config import (
    DB_PASSWORD, DB_USER, DB_HOST, DB_PORT, DB_NAME,
    REDIS_HOST, REDIS_PORT
)


class Settings(BaseSettings):
    db_url: str = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?async_fallback=True"
    db_cache_url: str = f"redis://{REDIS_HOST}:{REDIS_PORT}"
    db_echo: bool = True


settings = Settings()

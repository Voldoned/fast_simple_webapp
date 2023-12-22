from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis
from contextlib import asynccontextmanager

from app.api_v1.articles.router import router as router_articles
from app.users.router import router as router_users

from app.core.db_helper import db_helper
from app.core.base import Base
from app.core.db_settings import db_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(
        db_settings.db_cache_url,
        encoding="utf8",
        decode_responses=True
    )
    FastAPICache.init(RedisBackend(redis), prefix="api:cache")

    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

app = FastAPI(lifespan=lifespan)

# origins = [
#     "http://localhost:8000"
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(router_articles)
app.include_router(router_users)

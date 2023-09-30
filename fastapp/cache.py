from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

from config import REDIS_HOST, REDIS_PORT


async def init_redis():
    redis = aioredis.from_url(
            f"redis://{REDIS_HOST}:{REDIS_PORT}",
            encoding="utf8",
            decode_responses=True
    )
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
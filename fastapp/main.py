import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.router import router
from cache import init_redis
from app.database import init_models

app = FastAPI()

origins = [
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.on_event("startup")
async def on_startup():
    await init_models()
    await init_redis()


if __name__ == '__main__':
    uvicorn.run(
        app,
        log_level="info",
        host="0.0.0.0",
        port=8000,
        proxy_headers=True
    )

from typing import AsyncGenerator

from sqlalchemy import NullPool, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

# Create a sqlite engine instance
URL_DB = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_async_engine(URL_DB, poolclass=NullPool, echo=True,)

# Create a DeclarativeMeta instance
Base = declarative_base()

metadata = MetaData()

async_session = sessionmaker(engine, class_=AsyncSession,expire_on_commit=False)


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

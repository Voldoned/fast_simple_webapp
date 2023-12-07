from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_cache.decorator import cache

from app.core.db_helper import db_helper
from app.core.db_utils import statement_select_all_from_table
from app.core.base_crud import BaseAsyncCRUD
from .models import Article
from .schemas.response_schemas import (
    ArticleResponseSchema,
    ArticlesResponseSchema,
    ArticleCountResponseSchema,
    ArticleCreateResponseSchema
)
from .schemas.request_schemas import ArticleCreateBaseRequestSchema

router = APIRouter(
    prefix="/articles",
    tags=["articles"]
)

crud = BaseAsyncCRUD(Article)


@router.get(
    "/",
    response_model=ArticlesResponseSchema
)
@cache(expire=60 * 5)
async def get_articles(session: AsyncSession = Depends(
    db_helper.scoped_session_dependency
)):
    return await crud.get_all_raws_from_tabel(session)


@router.get(
    "/head/{count}",
    response_model=ArticlesResponseSchema
)
@cache(expire=60 * 5)
async def get_head_articles(count: int,
                            session: AsyncSession = Depends(
                                db_helper.scoped_session_dependency
                            )):
    return await crud.get_head_rows(count, session)


@router.get(
    "/user/{id}",
    response_model=ArticleResponseSchema
)
@cache(expire=60 * 5)
async def get_article_with_id(id: int,
                              session: AsyncSession = Depends(
                                  db_helper.scoped_session_dependency
                              )):
    return await crud.get_row_with_id(id, session)


@router.get(
    "/count_articles",
    response_model=ArticleCountResponseSchema
)
@cache(expire=60 * 5)
async def get_count_of_articles(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    statement = await statement_select_all_from_table(Article)
    result = await session.execute(statement)
    return {
        "count_articles": len(result.scalars().all())
    }


@router.post(
    "/add",
    response_model=ArticleCreateResponseSchema
)
async def add_article(new_article: ArticleCreateBaseRequestSchema,
                      session: AsyncSession = Depends(
                          db_helper.scoped_session_dependency
                      )):
    return await crud.create_row(new_article, session)

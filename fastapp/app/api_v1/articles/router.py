from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from fastapi_cache.decorator import cache

from config import settings

from .schemas.response.update_response import ArticleUpdateResponseSchema
from ...core.db_helper import db_helper
from ...core.db_utils import statement_select_all_from_table
from ...core.base_crud import BaseAsyncCRUD

from .models import Article
from .dependencies import article_by_id

from .schemas.response.article_response import ArticleResponseSchema
from .schemas.response.articles_response import ArticlesResponseSchema
from .schemas.response.count_response import ArticleCountResponseSchema
from .schemas.response.create_response import ArticleCreateResponseSchema
from .schemas.response.article_users_response import (
    ArticlesWithUsersResponseSchema
)
from .schemas.response.delete_response import ArticleDeleteResponseSchema

from .schemas.request.create_request import ArticleCreateRequestSchema
from .schemas.request.update_request import ArticleUpdateRequestSchema

router = APIRouter(
    prefix="/articles",
    tags=["articles"]
)

crud = BaseAsyncCRUD(Article)


@router.get("/", response_model=ArticlesResponseSchema)
@cache(expire=settings.expire_cache)
async def get_all_articles(session: AsyncSession = Depends(
    db_helper.scoped_session_dependency
)):
    return await crud.get_all_tabel(session)


@router.get("/head/{count}", response_model=ArticlesResponseSchema)
@cache(expire=settings.expire_cache)
async def get_head_count_articles(
    count: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.get_head_rows(count, session)


@router.get("/article/{id}", response_model=ArticleResponseSchema)
@cache(expire=settings.expire_cache)
async def get_article_by_id(
    article: Article = Depends(article_by_id)
):
    return article


@router.get("/count_articles", response_model=ArticleCountResponseSchema)
@cache(expire=settings.expire_cache)
async def get_count_of_articles(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    statement = await statement_select_all_from_table(table=Article)
    result = await session.execute(statement)
    return {
        "count_articles": len(result.scalars().all())
    }


@router.get("/all", response_model=ArticlesWithUsersResponseSchema)
@cache(expire=settings.expire_cache)
async def get_articles_user(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    query = (await statement_select_all_from_table(table=Article)).options(
        joinedload(Article.user)
    )
    result = await session.execute(query)
    list_rows = result.unique().scalars().all()
    return list_rows


@router.post(
    "/add",
    response_model=ArticleCreateResponseSchema
)
async def add_article(new_article: ArticleCreateRequestSchema,
                      session: AsyncSession = Depends(
                          db_helper.scoped_session_dependency
                      )):
    return await crud.create_row(schema=new_article, session=session)


@router.put(
    "/update",
    response_model=ArticleUpdateResponseSchema
)
async def update_article(
    article_update: ArticleUpdateRequestSchema,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_row(
        session=session,
        schema=article_update,
        is_partial=False
    )


# @router.put(
#     "/update/partial",
#     response_model=ArticleUpdateResponseSchema
# )
# async def partial_update_article(
#     article_update: ArticleUpdateRequestSchema,
#     session: AsyncSession = Depends(db_helper.scoped_session_dependency)
# ):
#     return await crud.update_row(
#         session=session,
#         schema=article_update,
#         is_partial=True
#     )


@router.delete("/delete/{id}", response_model=ArticleDeleteResponseSchema)
async def delete_article(
    article_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.delete_row(id=article_id, session=session)


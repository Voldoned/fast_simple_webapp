from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from fastapi_cache.decorator import cache

from config import settings

from .dependencies import user_by_id


from ..core.db_helper import db_helper
from ..core.db_utils import statement_select_all_from_table
from ..core.base_crud import BaseAsyncCRUD

from .models import User

from .schemas.response.user_response import UserResponseSchema
from .schemas.response.users_response import UsersResponseSchema
from .schemas.response.count_response import UserCountResponseSchema
from .schemas.response.user_article_response import (
    UsersWithArticlesResponseSchema
)
from .schemas.response.create_response import UserCreateResponseSchema
from .schemas.response.delete_response import UserDeleteResponseSchema
from .schemas.response.update_response import UserUpdateResponseSchema
from .schemas.response.update_partial_response import (
    UserPartialUpdateResponseSchema
)

from .schemas.request.create_request import UserCreateRequestSchema
from .schemas.request.update_request import UserUpdateRequestSchema
from .schemas.request.update_partial_request import (
    UserPartialUpdateRequestSchema
)


router = APIRouter(
    prefix="/users",
    tags=["users"]
)

crud = BaseAsyncCRUD(User)


@router.get("/", response_model=UsersResponseSchema)
@cache(expire=settings.expire_cache)
async def get_users(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.get_all_tabel(session)


@router.get("/head/{count}", response_model=UsersResponseSchema)
@cache(expire=settings.expire_cache)
async def get_first_users(
    count: int,
    session: AsyncSession = Depends(
        db_helper.scoped_session_dependency
    )
):
    return await crud.get_head_rows(count, session)


@router.get("/user/{id}", response_model=UserResponseSchema)
@cache(expire=settings.expire_cache)
async def get_user_by_id(user: User = Depends(user_by_id)):
    return user


@router.get("/count_users", response_model=UserCountResponseSchema)
@cache(expire=settings.expire_cache)
async def get_count_of_users(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    """
    Get count registered users.
    """
    statement = await statement_select_all_from_table(User)
    result = await session.execute(statement)
    return {
        "count_users": len(result.scalars().all())
    }


@router.get(
    "/all",
    # response_model=UsersWithArticlesResponseSchema
)
@cache(expire=settings.expire_cache)
async def get_user_articles(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    query = (await statement_select_all_from_table(User)).options(
        selectinload(User.articles)
    )
    result = await session.execute(query)
    return result.unique().scalars().all()


@router.post("/add", response_model=UserCreateResponseSchema)
async def add_user(
    new_user: UserCreateRequestSchema,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.create_row(new_user, session)


@router.put(
    "/update",
    response_model=UserUpdateResponseSchema
)
async def update_article(
    article_update: UserUpdateRequestSchema,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_row(
        session=session,
        schema=article_update,
        is_partial=False
    )


# @router.put(
#     "/update/partial",
#     response_model=UserPartialUpdateResponseSchema
# )
# async def partial_update_article(
#     article_update: UserPartialUpdateRequestSchema,
#     session: AsyncSession = Depends(db_helper.scoped_session_dependency)
# ):
#     return await crud.update_row(
#         session=session,
#         schema=article_update,
#         is_partial=True
#     )


@router.delete("/delete/{id}", response_model=UserDeleteResponseSchema)
async def delete_article(
    id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.delete_row(id=id, session=session)

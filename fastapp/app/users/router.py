from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_cache.decorator import cache

from app.core.db_helper import db_helper
from app.core.db_utils import statement_select_all_from_table
from app.core.base_crud import BaseAsyncCRUD
from .models import User
from .schemas.response_schemas import (
    UserResponseSchema,
    UsersResponseSchema,
    UserCountResponseSchema,
    UserCreateResponseSchema
)
from .schemas.request_schemas import UserCreateRequestSchema

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

crud = BaseAsyncCRUD(User)


@router.get("/", response_model=UsersResponseSchema)
@cache(expire=60 * 5)
async def get_users(session: AsyncSession = Depends(
    db_helper.scoped_session_dependency
)):
    return await crud.get_all_raws_from_tabel(session)


@router.get("/head/{count}", response_model=UsersResponseSchema)
@cache(expire=60 * 5)
async def get_first_users(count: int,
                          session: AsyncSession = Depends(
                              db_helper.scoped_session_dependency
                          )):
    return await crud.get_head_rows(count, session)


@router.get("/user/{id}", response_model=UserResponseSchema)
@cache(expire=60 * 5)
async def get_user_with_id(id: int, session: AsyncSession = Depends(
    db_helper.scoped_session_dependency
)):
    return await crud.get_row_with_id(id, session)


@router.get("/count_users", response_model=UserCountResponseSchema)
@cache(expire=60 * 5)
async def get_count_of_users(session: AsyncSession = Depends(
    db_helper.scoped_session_dependency
)):
    """
    Get count registered users.
    """
    statement = await statement_select_all_from_table(User)
    result = await session.execute(statement)
    return {
        "count_users": len(result.scalars().all())
    }


@router.post("/add", response_model=UserCreateResponseSchema)
async def add_user(new_user: UserCreateRequestSchema,
                   session: AsyncSession = Depends(
                       db_helper.scoped_session_dependency
                   )):
    return await crud.create_row(new_user, session)

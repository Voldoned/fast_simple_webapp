from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_cache.decorator import cache

from .database import get_async_session
from .models import User
from .schemas import UserCreateSchema

router = APIRouter(
    prefix="/get_data",
    tags=["get_data"]
)


def statement_select_all_from_user():
    return select(User).order_by(User.id)


@router.get("/users")
@cache(expire=60)
async def get_users(session: AsyncSession = Depends(get_async_session)):
    """
    Get list of all users.
    """
    statement = statement_select_all_from_user()
    result = await session.execute(statement)
    return result.scalars().all()


@router.get("/users/first/{count}")
@cache(expire=60)
async def get_first_users(count: int,
                          session: AsyncSession = Depends(get_async_session)):
    """
    Get first {count} users from all users.
    """
    statement = statement_select_all_from_user()
    result = await session.execute(statement)
    typized_result = result.scalars().all()

    # Если введеное число будет отрицательным, то срез будет с конца списка.
    # Если введенное число будет равно нулю, результатом будет пустой список,
    # поэтому вызываем исключение некорретных входных данных
    if count > 0:
        return typized_result[:count]
    elif count < 0:
        return typized_result[count:]
    else:
        raise HTTPException(
            status_code=406,
            detail="Empty result. Please, enter nonzero value of 'count'",

        )


@router.get("/user/{id}")
@cache(expire=60)
async def get_user_with_id(id: int,
                           session: AsyncSession = Depends(get_async_session)):
    """
    Get user with id={id}.
    """
    statement = select(User).where(User.id == id)
    result = await session.execute(statement)
    return result.scalars().all()


@router.post("/user/add")
async def add_user(new_user: UserCreateSchema,
                   session: AsyncSession = Depends(get_async_session)):
    """
    Add new user.
    """
    input_data = new_user.model_dump()
    statement = insert(User).values(**input_data)
    await session.execute(statement)
    await session.commit()  # End transaction
    return {
        "status": "success",
        "new_user": input_data
    }

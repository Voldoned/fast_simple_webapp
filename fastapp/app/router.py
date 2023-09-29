from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.orm import Session, Query

from fastapi_cache.decorator import cache

from .database import get_session
from .models import User, user
from .schemas import UserCreate

router = APIRouter(
    prefix="/get_data",
    tags=["get_data"]
)


def select_all_from_user(session: Session) -> Query:
    return session.query(User)


@router.get("/users")
@cache(expire=60)
def get_users(session: Session = Depends(get_session)):
    return select_all_from_user(session).all()


@router.get("/users/first/{count}")
@cache(expire=60)
def get_first_users(count: int, session: Session = Depends(get_session)):
    return select_all_from_user(session).all()[:count]


@router.get("/user/{id}")
@cache(expire=60)
def get_user_with_id(id: int, session: Session = Depends(get_session)):
    return session.query(User).where(User.id == id).all()


@router.post("/user/add")
def add_user(new_user: UserCreate, session: Session = Depends(get_session)):
    input_data = new_user.model_dump()
    statement = insert(User).values(**input_data)
    session.execute(statement)
    session.commit()  # End transaction
    return {
        "status": "success",
        "new_user": input_data
    }

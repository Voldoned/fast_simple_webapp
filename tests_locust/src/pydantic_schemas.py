from datetime import datetime
from typing import List, Sequence

from pydantic import BaseModel


class UserSchema(BaseModel):
    email: str
    username: str
    password: str
    registered_at: datetime


class UsersSchema(BaseModel):
    data: List[UserSchema]


class CreateUserResponseSchema(BaseModel):
    status: str = "success"
    new_data: UserSchema


class ArticleSchema(BaseModel):
    title: str
    text: str
    annotation: str
    published_at: datetime


class ArticlesSchema(BaseModel):
    data: List[ArticleSchema]


class CreateArticleResponseSchema(BaseModel):
    status: str = "success"
    new_data: ArticleSchema


class ErrorMessageSchema(BaseModel):
    detail: List[str]

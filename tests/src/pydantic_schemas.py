from datetime import datetime
from typing import List, Sequence

from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    email: str
    username: str


class UserSchema(UserBaseSchema):
    id: int
    registered_at: datetime


class UsersSchema(BaseModel):
    data: List[UserSchema]


class CreateUserResponse(BaseModel):
    status: str = "success"
    new_data: UserSchema


class ArticleSchema(BaseModel):
    title: str
    text: str
    annotation: str


class ArticlesSchema(BaseModel):
    data: List[ArticleSchema]


class CreateArticleResponseSchema(BaseModel):
    status: str = "success"
    new_data: ArticleSchema


class ErrorMessageSchema(BaseModel):
    detail: str | list

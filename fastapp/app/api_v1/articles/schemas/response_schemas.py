from typing import List

from app.core.base_response_schema import BaseResponseSchema

from .base_schema import ArticleBaseSchema
from .request_schemas import ArticleBaseRequestSchema


class ArticleBaseResponseSchema(ArticleBaseSchema, BaseResponseSchema):
    pass


class ArticleResponseSchema(ArticleBaseResponseSchema):
    id: int


class ArticlesResponseSchema(BaseResponseSchema):
    data: List[ArticleResponseSchema]


class ArticleCreateResponseSchema(BaseResponseSchema):
    status: str
    new_data: ArticleBaseRequestSchema


class ArticleCountResponseSchema(BaseResponseSchema):
    count_users: int

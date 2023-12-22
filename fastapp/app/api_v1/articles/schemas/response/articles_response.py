from typing import List

from .base_response import ArticleBaseResponseSchema
from .....core.base_response_schema import BaseResponseSchema


class ArticlesResponseSchema(BaseResponseSchema):
    data: List[ArticleBaseResponseSchema]

from .base_response import ArticleBaseResponseSchema
from .....core.base_response_schema import BaseResponseSchema


class ArticleUpdateResponseSchema(BaseResponseSchema):
    status: str
    updated_data: ArticleBaseResponseSchema

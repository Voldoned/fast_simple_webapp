from .base_response import ArticleBaseResponseSchema
from .....core.base_response_schema import BaseResponseSchema


class ArticleDeleteResponseSchema(BaseResponseSchema):
    status: str
    deleted_data: ArticleBaseResponseSchema

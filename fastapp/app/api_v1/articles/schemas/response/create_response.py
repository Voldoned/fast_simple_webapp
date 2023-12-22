from ..request.create_request import ArticleCreateRequestSchema
from .....core.base_response_schema import BaseResponseSchema


class ArticleCreateResponseSchema(BaseResponseSchema):
    status: str
    new_data: ArticleCreateRequestSchema

from .base_request import ArticleBaseRequestSchema
from ..base_schema import ArticleBaseSchema


class ArticleCreateRequestSchema(ArticleBaseSchema):
    user_id: int
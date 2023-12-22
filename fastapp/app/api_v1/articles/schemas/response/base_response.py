from datetime import datetime

from ..base_schema import ArticleBaseSchema


class ArticleBaseResponseSchema(ArticleBaseSchema):
    id: int
    published_at: datetime
    user_id: int
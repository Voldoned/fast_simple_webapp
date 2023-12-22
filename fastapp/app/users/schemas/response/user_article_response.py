from datetime import datetime
from typing import List

from ....api_v1.articles.schemas.base_schema import ArticleBaseSchema
from ....users.schemas.base_schema import UserBaseSchema


class ArticleViewSchema(ArticleBaseSchema):
    id: int
    published_at: datetime
    user_id: int


class UsersWithArticlesResponseSchema(UserBaseSchema):
    id: int
    registered_at: datetime
    articles: List[ArticleViewSchema] = []

from .....users.schemas.base_schema import UserBaseSchema
from .base_response import ArticleBaseResponseSchema


class UserViewSchema(UserBaseSchema):
    id: int
    article_id: int


class ArticlesWithUsersResponseSchema(ArticleBaseResponseSchema):
    user: UserViewSchema

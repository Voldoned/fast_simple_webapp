from ....core.base_response_schema import BaseResponseSchema


class ArticleBaseSchema(BaseResponseSchema):
    title: str
    annotation: str
    text: str
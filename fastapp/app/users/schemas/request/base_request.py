from ..base_schema import UserBaseSchema


class UserBaseRequestSchema(UserBaseSchema):
    password: str

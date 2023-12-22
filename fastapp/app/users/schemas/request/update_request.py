from .base_request import UserBaseRequestSchema


class UserUpdateRequestSchema(UserBaseRequestSchema):
    id: int

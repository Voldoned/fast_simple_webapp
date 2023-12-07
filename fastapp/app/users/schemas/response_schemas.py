from typing import List

from app.core.base_response_schema import BaseResponseSchema

from .base_schema import UserBaseSchema
from .request_schemas import UserRequestSchema


class UserBaseResponseSchema(UserBaseSchema, BaseResponseSchema):
    pass


class UserResponseSchema(UserBaseResponseSchema):
    id: int


class UsersResponseSchema(BaseResponseSchema):
    data: List[UserResponseSchema]


class UserCreateResponseSchema(BaseResponseSchema):
    status: str
    new_data: UserRequestSchema


class UserCountResponseSchema(BaseResponseSchema):
    count_users: int

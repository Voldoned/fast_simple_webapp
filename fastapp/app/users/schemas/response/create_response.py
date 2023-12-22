from .user_response import UserResponseSchema
from ....core.base_response_schema import BaseResponseSchema


class UserCreateResponseSchema(BaseResponseSchema):
    status: str
    new_data: UserResponseSchema

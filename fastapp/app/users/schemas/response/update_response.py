from .base_response import UserBaseResponseSchema
from ....core.base_response_schema import BaseResponseSchema


class UserUpdateResponseSchema(BaseResponseSchema):
    status: str
    updated_data: UserBaseResponseSchema

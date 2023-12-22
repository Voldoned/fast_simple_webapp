from .base_response import UserBaseResponseSchema
from ....core.base_response_schema import BaseResponseSchema


class UserDeleteResponseSchema(BaseResponseSchema):
    status: str
    deleted_data: UserBaseResponseSchema

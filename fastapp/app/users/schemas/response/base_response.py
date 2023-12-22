from datetime import datetime

from ....core.base_response_schema import BaseResponseSchema
from ..base_schema import UserBaseSchema


class UserBaseResponseSchema(UserBaseSchema, BaseResponseSchema):
    id: int
    registered_at: datetime
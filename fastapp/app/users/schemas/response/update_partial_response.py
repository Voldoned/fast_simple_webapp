from typing import Optional
from .base_response import UserBaseResponseSchema


class UserPartialUpdateResponseSchema(UserBaseResponseSchema):
    email: Optional[str]
    username: Optional[str]

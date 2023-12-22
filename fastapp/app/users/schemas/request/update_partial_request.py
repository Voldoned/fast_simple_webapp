from typing import Optional
from .base_request import UserBaseRequestSchema


class UserPartialUpdateRequestSchema(UserBaseRequestSchema):
    id: int
    email: Optional[str]
    username: Optional[str]
    password: Optional[str]

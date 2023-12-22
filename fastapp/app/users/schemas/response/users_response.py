from typing import List
from pydantic import BaseModel

from .user_response import UserResponseSchema


class UsersResponseSchema(BaseModel):
    data: List[UserResponseSchema]

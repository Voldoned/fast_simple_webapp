from datetime import datetime

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    email: str
    username: str
    password: str
    registered_at: datetime


class CreateUserResponse(BaseModel):
    status: str = "success"
    new_user: UserSchema

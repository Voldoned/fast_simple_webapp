from datetime import datetime

from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    email: str
    username: str
    password: str
    registered_at: datetime
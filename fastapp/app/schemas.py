from datetime import datetime
from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    id: int
    email: str
    username: str
    password: str
    registered_at: datetime
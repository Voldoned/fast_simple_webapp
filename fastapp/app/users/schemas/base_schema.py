from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    email: str
    username: str


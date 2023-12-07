from datetime import datetime

from pydantic import BaseModel


class ArticleBaseSchema(BaseModel):
    title: str
    text: str
    annotation: str
    published_at: datetime
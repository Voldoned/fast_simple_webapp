from datetime import datetime

from sqlalchemy import String, TIMESTAMP, Column, Text

from app.core.base import Base


class Article(Base):
    # __table_args__ = {'extend_existing': True}

    title: str = Column(String, nullable=False)
    text: str = Column(Text, nullable=False)
    annotation: str = Column(Text, nullable=False)
    published_at: datetime = Column(TIMESTAMP, default=datetime.utcnow)

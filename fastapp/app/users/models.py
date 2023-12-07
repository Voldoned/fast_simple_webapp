from datetime import datetime

from sqlalchemy import String, TIMESTAMP, Column

from app.core.base import Base


class User(Base):
    # __table_args__ = {'extend_existing': True}

    email: str = Column(String, nullable=False)
    username: str = Column(String, nullable=False)
    password: str = Column(String, nullable=False)
    registered_at: datetime = Column(TIMESTAMP, default=datetime.utcnow)

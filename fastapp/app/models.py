from datetime import datetime

from sqlalchemy import Integer, String, TIMESTAMP, Column

from .database import Base


class User(Base):
    __tablename__ = "user"
    # __table_args__ = {'extend_existing': True}

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String, nullable=False)
    username: str = Column(String, nullable=False)
    password: str = Column(String, nullable=False)
    registered_at: datetime = Column(TIMESTAMP, default=datetime.utcnow)

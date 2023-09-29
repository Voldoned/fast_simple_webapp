from datetime import datetime

from sqlalchemy import Integer, String, TIMESTAMP, Table, Column

from .database import metadata, Base

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
)


class User(Base):
    __tablename__ = "user"
    __table_args__ = {'extend_existing': True}

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String, nullable=False)
    username: str = Column(String, nullable=False)
    password: str = Column(String, nullable=False)
    registered_at: datetime = Column(TIMESTAMP, default=datetime.utcnow)

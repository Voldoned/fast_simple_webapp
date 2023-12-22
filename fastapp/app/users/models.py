from datetime import datetime
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from ..core.base import Base


class User(Base):
    # __table_args__ = {'extend_existing': True}

    email: Mapped[str]
    username: Mapped[str]
    password: Mapped[str]
    registered_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    articles: Mapped[List["Article"]] = relationship(back_populates="user")

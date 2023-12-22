from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from ...core.base import Base


class Article(Base):
    # __table_args__ = {'extend_existing': True}

    title: Mapped[str]
    text: Mapped[str]
    annotation: Mapped[str]
    published_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )
    user: Mapped["User"] = relationship(back_populates="articles")

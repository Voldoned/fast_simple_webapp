from sqlalchemy import Column, Integer, Sequence
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = Column(
        "id",
        Integer,
        Sequence("id_seq", start=1),
        primary_key=True,
    )

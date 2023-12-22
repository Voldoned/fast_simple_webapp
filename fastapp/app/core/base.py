from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    def __repr__(self):
        cols = []
        for col in self.__table__.columns.keys():
            cols.append(col)

        return f"<{self.__class__.__name__} {', '.join(cols)}>"

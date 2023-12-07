from sqlalchemy import select

from .base import Base


async def statement_select_all_from_table(table: Base):
    """
    Query for get ordered list of rows in tabel by id
    """
    return select(table).order_by(table.id)
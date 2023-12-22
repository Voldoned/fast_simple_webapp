from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends

from .models import Article
from ...core.base_crud import BaseAsyncCRUD
from ...core.db_helper import db_helper


async def article_by_id(
    id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await BaseAsyncCRUD(Article).get_row_with_id(id, session)

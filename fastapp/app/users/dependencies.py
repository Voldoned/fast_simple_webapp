from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends

from .models import User
from ..core.base_crud import BaseAsyncCRUD
from ..core.db_helper import db_helper


async def user_by_id(
    id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await BaseAsyncCRUD(User).get_row_with_id(id, session)

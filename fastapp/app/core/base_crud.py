from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy import select, insert
from sqlalchemy.exc import DBAPIError
from sqlalchemy.ext.asyncio import AsyncSession

from .base import Base
from .db_utils import statement_select_all_from_table


class BaseAsyncCRUD:

    def __init__(self, model: Base):
        self.model = model

    async def get_all_tabel(self, session: AsyncSession):
        statement = await statement_select_all_from_table(self.model)
        result = await session.execute(statement)
        return {
            "data": list(result.scalars().all())
        }

    async def get_head_rows(self, count: int, session: AsyncSession):
        statement = await statement_select_all_from_table(self.model)

        result = await session.execute(statement)
        typized_result = list(result.scalars().all())

        # Если введеное число будет отрицательным, то срез будет с конца списка.
        # Если введенное число будет равно нулю, результатом будет пустой
        # список, поэтому вызываем исключение некорретных входных данных
        if count > 0:
            return {
                "data": typized_result[:count]
            }
        elif count < 0:
            return {
                "data": typized_result[count:]
            }
        raise HTTPException(
            status_code=406,
            detail="Empty result. Please, enter nonzero value of 'count'",
        )

    async def get_row_with_id(self, id: int, session: AsyncSession):
        statement = select(self.model).where(self.model.id == id)
        result = await session.execute(statement)
        return result.scalars().all()[0]

    async def create_row(self, schema: BaseModel, session: AsyncSession):
        try:
            input_data = self.model(**schema.model_dump())
            # statement = insert(self.model).values(**input_data)
            session.add(input_data)
            await session.commit()  # End transaction
            # await session.refresh()
            return {
                "status": "success",
                "new_data": input_data
            }

        except DBAPIError as ex:
            raise HTTPException(
                status_code=400,
                detail=f"{ex}"
            )

        except Exception as ex:
            raise HTTPException(
                status_code=500,
                detail=f"{ex}"
            )

    async def update_row(self,
                         schema: BaseModel,
                         session: AsyncSession,
                         is_partial: bool = False):
        try:
            row = await self.get_row_with_id(id=schema.id, session=session)
            for name, value in schema.model_dump(exclude_unset=is_partial).items():
                setattr(row, name, value)
            await session.commit()
            # await session.refresh()
            return {
                "status": "success",
                "updated_data": row
            }

        except DBAPIError as ex:
            raise HTTPException(
                status_code=400,
                detail=f"{ex}"
            )

        except Exception as ex:
            raise HTTPException(
                status_code=500,
                detail=f"{ex}"
            )

    async def delete_row(self, id, session: AsyncSession):
        try:
            row = await self.get_row_with_id(id=id, session=session)
            await session.delete(row)
            await session.commit()
            # await session.refresh()
            return {
                "status": "success",
                "deleted_data": row
            }

        except DBAPIError as ex:
            raise HTTPException(
                status_code=400,
                detail=f"{ex}"
            )

        except Exception as ex:
            raise HTTPException(
                status_code=500,
                detail=f"{ex}"
            )

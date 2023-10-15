from fastapi import HTTPException
from sqlalchemy import select, insert
from sqlalchemy.exc import DBAPIError
from sqlalchemy.ext.asyncio import AsyncSession

from .db_utils import statement_select_all_from_table


class BaseAsyncCRUD:

    def __init__(self, model):
        self.model = model

    async def get_all_raws_from_tabel(self, session: AsyncSession):
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
        return result.scalars().all()

    async def create_row(self, schema, session: AsyncSession):
        try:
            input_data = schema.model_dump()
            statement = insert(self.model).values(**input_data)
            await session.execute(statement)
            await session.commit()  # End transaction
            return {
                "status": "success",
                "new_data": input_data
            }
        except DBAPIError as e:
            raise HTTPException(
                status_code=400,
                detail=f"{e}"
            )
        except Exception as ex:
            raise HTTPException(
                status_code=500,
                detail=f"{ex}"
            )

from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.task.repository import get_all_tasks
from app.domain.task.schemas.response import TaskOut

async def handle_list_all_tasks(session: AsyncSession, user_id: UUID) -> list[TaskOut]:
    tasks = await get_all_tasks(session, user_id)
    return [TaskOut.model_validate(task) for task in tasks]

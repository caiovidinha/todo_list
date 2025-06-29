from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.task.schemas import TaskOut
from app.domain.task.repository import get_task_by_id


async def handle_get_task_by_id(session: AsyncSession, task_id: UUID, user_id: UUID) -> TaskOut | None:
    task = await get_task_by_id(session, task_id, user_id)
    if task is None:
        return None
    return TaskOut.model_validate(task)

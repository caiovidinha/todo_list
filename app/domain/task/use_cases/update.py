from uuid import UUID
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.task.repository import update_task
from app.domain.task.schemas.request import TaskUpdate
from app.domain.task.model import Task

async def handle_update_task(
    session: AsyncSession,
    task_id: UUID,
    user_id: UUID,
    task_update: TaskUpdate,
) -> Task | None:
    update_data = task_update.model_dump(exclude_unset=True)
    update_data["updated_at"] = datetime.utcnow()
    return await update_task(session, task_id, user_id, update_data)

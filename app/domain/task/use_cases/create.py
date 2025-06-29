from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.task.schemas import TaskCreate, TaskOut
from app.domain.task.repository import create_task


async def handle_create_task(
    session: AsyncSession,
    task_in: TaskCreate,
    user_id: str
) -> TaskOut:
    task = await create_task(session, task_in, user_id)
    return TaskOut.model_validate(task)

from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, select, update

from app.domain.task.model import Task
from app.domain.task.schemas import TaskCreate


async def get_all_tasks(session: AsyncSession, user_id: UUID) -> list[Task]:
    stmt = select(Task).where(Task.user_id == user_id)
    result = await session.execute(stmt)
    return result.scalars().all()


async def get_task_by_id(session: AsyncSession, task_id: UUID, user_id: UUID) -> Task | None:
    stmt = select(Task).where(Task.id == task_id, Task.user_id == user_id)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()


async def create_task(session: AsyncSession, task_in: TaskCreate, user_id: UUID) -> Task:
    task = Task(**task_in.model_dump(), user_id=user_id)
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task


async def update_task(
    session: AsyncSession,
    task_id: UUID,
    user_id: UUID,
    update_data: dict,
) -> Task | None:
    stmt = (
        update(Task)
        .where(Task.id == task_id, Task.user_id == user_id)
        .values(**update_data)
        .returning(Task)
    )
    result = await session.execute(stmt)
    await session.commit()
    return result.scalar_one_or_none()


async def delete_task_by_id(session: AsyncSession, task_id: UUID, user_id: UUID) -> bool:
    stmt = delete(Task).where(Task.id == task_id, Task.user_id == user_id)
    result = await session.execute(stmt)
    await session.commit()
    return result.rowcount > 0

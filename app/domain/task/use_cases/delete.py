from app.domain.task.repository import delete_task_by_id
from app.common.exceptions import TaskNotFoundException
from uuid import UUID

async def handle_delete_task(session, task_id: UUID, user_id: UUID) -> None:
    deleted = await delete_task_by_id(session, task_id, user_id)
    if not deleted:
        raise TaskNotFoundException(task_id)

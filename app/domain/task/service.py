from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.common.exceptions import TaskNotFoundException
from app.domain.task.schemas import TaskCreate, TaskOut
from app.domain.task.use_cases.create import handle_create_task
from app.domain.task.use_cases.delete import handle_delete_task
from app.domain.task.use_cases.get_by_id import handle_get_task_by_id
from app.domain.task.use_cases.list_all import handle_list_all_tasks
from app.domain.task.use_cases.update import handle_update_task
from app.domain.user.model import User
from app.core.logging import setup_logger

logger = setup_logger(__name__)


async def create_task_service(
    session: AsyncSession,
    task_in: TaskCreate,
    current_user: User
) -> TaskOut:
    logger.debug("Recebido payload de criação: %s", task_in.model_dump())
    task = await handle_create_task(session, task_in, current_user.id)
    logger.info("Tarefa criada com sucesso. ID: %s", task.id)
    return task


async def list_all_tasks_service(
    session: AsyncSession,
    current_user: User
):
    logger.info("Listando todas as tarefas do usuário %s", current_user.id)
    return await handle_list_all_tasks(session, current_user.id)


async def get_task_service(
    session: AsyncSession,
    task_id: UUID,
    current_user: User
) -> TaskOut:
    logger.info("Buscando tarefa com id=%s para o usuário %s", task_id, current_user.id)
    task = await handle_get_task_by_id(session, task_id, current_user.id)
    if not task:
        logger.warning("Tarefa com id=%s não encontrada para o usuário %s", task_id, current_user.id)
        raise TaskNotFoundException()
    return task


async def update_task_service(session, task_id, task_update, current_user):
    logger.info("Atualizando tarefa com id=%s para o usuário %s", task_id, current_user.id)
    task = await handle_update_task(session, task_id, current_user.id, task_update)
    if task is None:
        logger.warning("Tarefa com id=%s não encontrada para o usuário %s na atualização", task_id, current_user.id)
        raise TaskNotFoundException(task_id)
    logger.info("Tarefa com id=%s atualizada com sucesso", task.id)
    return task


async def delete_task_service(
    session: AsyncSession,
    task_id: UUID,
    current_user: User
) -> None:
    logger.info("Removendo tarefa com id=%s para o usuário %s", task_id, current_user.id)
    await handle_delete_task(session, task_id, current_user.id)
    logger.info("Tarefa com id=%s removida com sucesso", task_id)

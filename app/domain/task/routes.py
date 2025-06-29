from uuid import UUID
from fastapi import APIRouter, Depends, Path, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from app.domain.task.schemas import TaskCreate, TaskOut
from app.domain.task.schemas.request import TaskUpdate
from app.domain.task.service import (
    create_task_service,
    get_task_service,
    list_all_tasks_service,
    update_task_service,
    delete_task_service
)
from app.auth.dependencies import get_current_user
from app.domain.user.model import User
from app.core.db import get_db_session

router = APIRouter()

@router.get("/", response_model=list[TaskOut])
async def list_tasks(
    session: Annotated[AsyncSession, Depends(get_db_session)],
    current_user: Annotated[User, Depends(get_current_user)]
):
    return await list_all_tasks_service(session, current_user)


@router.get("/{task_id}", response_model=TaskOut)
async def get_task(
    task_id: Annotated[UUID, Path()],
    session: Annotated[AsyncSession, Depends(get_db_session)],
    current_user: Annotated[User, Depends(get_current_user)]
):
    return await get_task_service(session, task_id, current_user)


@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
async def create_task(
    task_in: TaskCreate,
    session: Annotated[AsyncSession, Depends(get_db_session)],
    current_user: Annotated[User, Depends(get_current_user)]
):
    return await create_task_service(session, task_in, current_user)


@router.put("/{task_id}", response_model=TaskOut)
async def update_task(
    task_id: Annotated[UUID, Path()],
    task_update: TaskUpdate,
    session: Annotated[AsyncSession, Depends(get_db_session)],
    current_user: Annotated[User, Depends(get_current_user)]
):
    return await update_task_service(session, task_id, task_update, current_user)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: Annotated[UUID, Path()],
    session: Annotated[AsyncSession, Depends(get_db_session)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    await delete_task_service(session, task_id, current_user)
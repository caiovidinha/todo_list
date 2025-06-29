from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db_session
from app.domain.user.schemas import UserCreate, TokenResponse
from app.domain.user.service import create_user_service

router = APIRouter()


@router.post("/", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(get_db_session)
):
    return await create_user_service(session, user_in)

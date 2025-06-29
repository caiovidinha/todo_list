from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import uuid4

from app.domain.user.model import User
from app.domain.user.schemas import UserCreate


async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
    result = await session.execute(select(User).where(User.username == username))
    return result.scalar_one_or_none()


async def get_user_by_token(session: AsyncSession, token: str) -> User | None:
    result = await session.execute(select(User).where(User.token == token))
    return result.scalar_one_or_none()


async def create_user(session: AsyncSession, user_in: UserCreate, token: str) -> User:
    user = User(username=user_in.username, token=token)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

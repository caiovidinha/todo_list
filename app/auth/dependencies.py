from fastapi import Depends, Header
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db_session
from app.domain.user.repository import get_user_by_token
from app.common.exceptions import UnauthorizedException
from app.domain.user.model import User

bearer_scheme = HTTPBearer(auto_error=False)

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    session: AsyncSession = Depends(get_db_session),
) -> User:
    if credentials is None or not credentials.scheme.lower() == "bearer":
        raise UnauthorizedException()

    token = credentials.credentials
    user = await get_user_by_token(session, token)

    if not user:
        raise UnauthorizedException()

    return user

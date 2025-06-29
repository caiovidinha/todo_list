from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.user.schemas import UserCreate, TokenResponse
from app.domain.user.repository import get_user_by_username, create_user
from app.common.exceptions import UserAlreadyExistsException

import random
import string


def generate_token(length: int = 30) -> str:
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=length))

async def handle_create_user(session: AsyncSession, user_in: UserCreate) -> TokenResponse:
    existing = await get_user_by_username(session, user_in.username)
    if existing:
        raise UserAlreadyExistsException()
    token = generate_token()
    user = await create_user(session, user_in, token)
    return TokenResponse(access_token=user.token) 

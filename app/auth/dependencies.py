from fastapi import Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db_session
from app.domain.user.repository import get_user_by_token
from app.common.exceptions import UnauthorizedException
from app.domain.user.model import User

async def get_current_user(
    request: Request,
    session: AsyncSession = Depends(get_db_session),
) -> User:
    """
    Aqui vale ressaltar que usei essa extração 'manual' do bearer pois
    no desafio comentava sobre autenticação sem bibliotecas externas.
    Poderia usar o fastapi.security, mas pensei que pudesse ser considerado
    algo externo, então optei por uma validação manual do token. 
    """
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.lower().startswith("bearer "):
        raise UnauthorizedException()

    token = auth_header[7:].strip()
    if not token:
        raise UnauthorizedException()

    user = await get_user_by_token(session, token)

    if not user:
        raise UnauthorizedException()

    return user

from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.user.schemas import UserCreate, TokenResponse
from app.domain.user.use_cases.create import handle_create_user
from app.core.logging import setup_logger

logger = setup_logger(__name__)


async def create_user_service(session: AsyncSession, user_in: UserCreate) -> TokenResponse:
    logger.debug("Recebido payload de criação de usuário: %s", user_in.model_dump())
    token_response = await handle_create_user(session, user_in)
    logger.info("Usuário criado com sucesso. ID: %s", token_response.user_id)
    return token_response

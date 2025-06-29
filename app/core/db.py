from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from app.core.settings import get_settings

settings = get_settings()

engine = create_async_engine(settings.async_sqlalchemy_database_uri, echo=True)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)
Base = declarative_base()

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
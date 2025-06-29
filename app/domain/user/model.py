from uuid import uuid4
from sqlalchemy.orm import Mapped, mapped_column
from app.core.db import Base
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from uuid import UUID, uuid4
import datetime


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid4)
    username: Mapped[str] = mapped_column(unique=True, index=True)
    token: Mapped[str] = mapped_column(unique=True, index=True)
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow)

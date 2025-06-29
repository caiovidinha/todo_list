from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from uuid import UUID, uuid4
import datetime

from app.core.db import Base  

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid4)
    title: Mapped[str]
    description: Mapped[str]
    is_done: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow)
    updated_at: Mapped[datetime.datetime | None] = mapped_column(default=None)

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))


from datetime import datetime
from uuid import UUID
from .base import TaskBase
from pydantic import BaseModel

class TaskOut(TaskBase):
    id: UUID
    is_done: bool
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True

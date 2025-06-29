from datetime import datetime
from uuid import UUID
from pydantic import Field
from typing import Annotated
from .base import TaskBase

class TaskOut(TaskBase):
    id: Annotated[UUID, Field(..., example="e57c3a97-2e9c-4e8b-94ff-3a0ccf0ad245")]
    is_done: Annotated[bool, Field(..., example=False)]
    created_at: Annotated[datetime, Field(..., example="2024-06-28T12:34:56.789Z")]
    updated_at: Annotated[datetime | None, Field(None, example="2024-06-29T09:15:00.000Z")]

    class Config:
        from_attributes = True

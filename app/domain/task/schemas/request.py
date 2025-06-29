from pydantic import BaseModel
from .base import TaskBase

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    is_done: bool | None = None
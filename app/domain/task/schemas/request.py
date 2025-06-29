from pydantic import BaseModel, Field
from typing import Annotated
from .base import TaskBase

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Annotated[
        str | None, Field(None, min_length=1, max_length=255, example="Atualizar título")
    ]
    description: Annotated[
        str | None, Field(None, max_length=1000, example="Nova descrição detalhada")
    ]
    is_done: Annotated[
        bool | None, Field(None, example=True)
    ]

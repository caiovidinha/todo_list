from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    title: str = Field(..., max_length=255)
    description: str | None = None

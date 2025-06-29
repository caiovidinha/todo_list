from pydantic import BaseModel, Field
from typing import Annotated

class TaskBase(BaseModel):
    title: Annotated[
        str, 
        Field(..., min_length=1, max_length=255, example="Comprar pão")
    ]
    description: Annotated[
        str | None,
        Field(None, max_length=1000, example="Ir na padaria às 8h")
    ]

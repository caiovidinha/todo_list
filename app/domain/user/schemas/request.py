from pydantic import BaseModel, Field
from typing import Annotated

class UserCreate(BaseModel):
    username: Annotated[
        str, Field(..., min_length=3, max_length=30, example="caio.vidinha")
    ]

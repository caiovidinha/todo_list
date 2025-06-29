from pydantic import BaseModel, Field
from typing import Annotated

class TokenResponse(BaseModel):
    access_token: Annotated[str, Field(..., example="ABCDEF1234567890")]
    token_type: Annotated[str, Field(..., example="bearer")] = "bearer"

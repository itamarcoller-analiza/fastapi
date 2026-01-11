from pydantic import BaseModel, Field, EmailStr
from typing import Annotated, Optional


class User(BaseModel):
    id: Annotated[int, None] = None
    name: Annotated[str, Field(strict=True, min_length=1, max_length=50)]
    email: Annotated[EmailStr, Field(strict=True)]
    age: Optional[Annotated[int, Field(strict=True, ge=0, le=120)]] = None
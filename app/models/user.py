from typing import Optional

from pydantic import EmailStr
from sqlmodel import Field, SQLModel, AutoString

from app.models.base import BaseModel


class User(BaseModel, table=True):
    hashed_password: str
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    id: Optional[int] = Field(default=None, primary_key=True)



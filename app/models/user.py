from typing import Optional

from pydantic import EmailStr, BaseModel
from sqlmodel import Field, SQLModel, AutoString


class User(SQLModel, table=True):
    hashed_password: str
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    id: Optional[int] = Field(default=None, primary_key=True)


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserQuery(UserCreate):
    id: Optional[int] = None

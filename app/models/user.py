from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class User(SQLModel):
    id: str = Field(primary_key=True)
    email: EmailStr = Field(unique=True)
    hashed_password: str

from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime


class Singer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    country: Optional[str] = Field(default=None)
    birth_date: Optional[datetime] = Field(default=None)
    genre: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # 可以根据需要添加其他字段

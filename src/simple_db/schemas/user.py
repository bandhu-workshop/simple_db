from datetime import datetime
from typing import Optional

from pydantic import EmailStr
from sqlmodel import SQLModel


class UserCreate(SQLModel):
    email: EmailStr
    name: str


class UserUpdate(SQLModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = None


class UserResponse(SQLModel):
    id: Optional[int] = None
    email: str
    name: str
    created_at: datetime

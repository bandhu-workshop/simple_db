# schemas are based on API contracts, Input/Output models, better to use SQLModel here to handle relationships easily
from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel


class ItemCreate(SQLModel):
    name: str
    description: str = ""
    price: float
    tax: float = 0.0
    on_offer: bool = False


class ItemUpdate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    tax: Optional[float] = None
    on_offer: Optional[bool] = None


class ItemResponse(ItemCreate):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

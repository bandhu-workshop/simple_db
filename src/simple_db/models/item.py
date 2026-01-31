from datetime import datetime, timezone
from typing import Optional

from sqlmodel import Field, SQLModel


class Item(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str = ""
    price: float = Field(gt=0)
    tax: float = Field(default=0.0, ge=0)
    on_offer: bool = False
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: Optional[datetime] = Field(default=None)

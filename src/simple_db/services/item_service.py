from datetime import datetime, timezone

from sqlmodel import Session, select

from simple_db.models.item import Item
from simple_db.schemas.item import ItemCreate, ItemUpdate


def create_item(session: Session, item: ItemCreate):
    db_item = Item(**item.model_dump())
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


def get_item_by_id(session: Session, item_id: int):
    return session.exec(select(Item).where(Item.id == item_id)).first()


def update_item(session: Session, item_id: int, item_update: ItemUpdate):
    item = get_item_by_id(session, item_id)
    if not item:
        raise ValueError("Item not found")

    # Update only provided fields
    for key, value in item_update.model_dump(exclude_unset=True).items():
        setattr(item, key, value)  # setattr(x, 'y', v) is equivalent to x.y = v

    # Always update the updated_at timestamp
    item.updated_at = datetime.now(timezone.utc)

    session.add(item)
    session.commit()
    session.refresh(item)
    return item


def delete_item(session: Session, item_id: int):
    item = get_item_by_id(session, item_id)
    if not item:
        raise ValueError("Item not found")

    session.delete(item)
    session.commit()
    return {"message": "Item deleted successfully"}

from fastapi import APIRouter, Depends
from sqlmodel import Session

from simple_db.database import get_session
from simple_db.schemas.item import ItemCreate, ItemResponse, ItemUpdate
from simple_db.services.item_service import (
    create_item,
    delete_item,
    get_item_by_id,
    update_item,
)

router = APIRouter()


# create item endpoint
@router.post("/", response_model=ItemResponse)
def create_item_endpoint(item: ItemCreate, session: Session = Depends(get_session)):
    db_item = create_item(session, item)
    return db_item


# get item by id endpoint
@router.get("/{item_id}", response_model=ItemResponse)
def get_item_endpoint(item_id: int, session: Session = Depends(get_session)):
    item = get_item_by_id(session, item_id)
    if not item:
        raise ValueError("Item not found")
    return item


# update item endpoint
@router.put("/{item_id}", response_model=ItemResponse)
def update_item_endpoint(
    item_id: int, item_update: ItemUpdate, session: Session = Depends(get_session)
):
    item = update_item(session, item_id, item_update)
    return item


# delete item endpoint
@router.delete("/{item_id}", response_model=ItemResponse)
def delete_item_endpoint(item_id: int, session: Session = Depends(get_session)):
    result = delete_item(session, item_id)
    return result

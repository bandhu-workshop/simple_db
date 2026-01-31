from fastapi import APIRouter, Depends
from sqlmodel import Session

from simple_db.database import get_session
from simple_db.schemas.user import UserCreate, UserResponse
from simple_db.services.user_service import (
    create_user,
    delete_user,
    get_user_by_id,
    update_user,
)

router = APIRouter()


# create user endpoint
@router.post("/", response_model=UserResponse)
def create_user_endpoint(user: UserCreate, session: Session = Depends(get_session)):
    return create_user(session, user)


# read users endpoints
@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id_endpoint(user_id: int, session: Session = Depends(get_session)):
    return get_user_by_id(session, user_id)


# update user endpoint
@router.put("/{user_id}", response_model=UserResponse)
def update_user_endpoint(
    user_id: int, user_update: UserCreate, session: Session = Depends(get_session)
):
    return update_user(session, user_id, user_update)


# delete user endpoint
@router.delete("/{user_id}", response_model=dict)
def delete_user_endpoint(user_id: int, session: Session = Depends(get_session)):
    return delete_user(session, user_id)

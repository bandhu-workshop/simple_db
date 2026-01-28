from fastapi import APIRouter, Depends
from sqlmodel import Session

from simple_db.database import get_session
from simple_db.schemas.user import UserCreate, UserResponse
from simple_db.services.user_service import (
    create_user,
    get_all_users,
    get_random_user,
    get_user_by_id,
)

router = APIRouter()


@router.post("/", response_model=UserResponse)
def create_user_endpoint(user: UserCreate, session: Session = Depends(get_session)):
    return create_user(session, user)


@router.get("/", response_model=list[UserResponse])
def list_users(session: Session = Depends(get_session)):
    return get_all_users(session)


@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id_endpoint(user_id: int, session: Session = Depends(get_session)):
    return get_user_by_id(session, user_id)


@router.get("/random_user", response_model=UserResponse)
def get_random_user_endpoint(session: Session = Depends(get_session)):
    return get_random_user(session)

from sqlalchemy import func
from sqlmodel import Session, select

from simple_db.models.user import User
from simple_db.schemas.user import UserCreate


def create_user(session: Session, user: UserCreate):
    db_user = User(email=user.email, name=user.name)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def get_all_users(session: Session):
    return session.exec(select(User)).all()


def get_user_by_id(session: Session, user_id: int):
    return session.exec(select(User).where(User.id == user_id)).first()


def get_random_user(session: Session):
    return session.exec(select(User).order_by(func.random()).limit(1)).first()

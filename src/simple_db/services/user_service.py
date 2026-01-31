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


def get_random_user(session: Session) -> User:
    user = session.exec(select(User).order_by(func.random()).limit(1)).first()

    if not user:
        raise ValueError("No users in database")

    return user


def update_user(session: Session, user_id: int, user_update: UserCreate):
    user = get_user_by_id(session, user_id)
    if not user:
        raise ValueError("User not found")

    user.email = user_update.email
    user.name = user_update.name

    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def delete_user(session: Session, user_id: int):
    user = get_user_by_id(session, user_id)
    if not user:
        raise ValueError("User not found")

    session.delete(user)
    session.commit()
    return {"message": "User deleted successfully"}

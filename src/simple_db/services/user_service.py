from sqlmodel import Session, select

from simple_db.models.user import User
from simple_db.schemas.user import UserCreate, UserUpdate


def create_user(session: Session, user: UserCreate):
    db_user = User(email=str(user.email), name=user.name)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def get_user_by_id(session: Session, user_id: int):
    return session.exec(select(User).where(User.id == user_id)).first()


def update_user(session: Session, user_id: int, user_update: UserUpdate):
    user = get_user_by_id(session, user_id)
    if not user:
        raise ValueError("User not found")

    # Update only provided fields
    for key, value in user_update.model_dump(exclude_unset=True).items():
        setattr(user, key, value)  # setattr(x, 'y', v) is equivalent to x.y = v

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

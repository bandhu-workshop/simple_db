from faker import Faker
from sqlmodel import Session

from simple_db.database import engine
from simple_db.models.user import User

fake = Faker()


def create_fake_users(session: Session, num_users: int = 20):
    users = []

    for _ in range(num_users):
        user = User(
            email=fake.unique.email(),
            name=fake.name(),
        )
        users.append(user)

    session.add_all(users)
    session.commit()

    print(f"✅ Inserted {num_users} fake users into database")


def main():
    with Session(engine) as session:
        create_fake_users(session, num_users=10)


if __name__ == "__main__":
    main()

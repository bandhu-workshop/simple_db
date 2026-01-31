import random

from faker import Faker
from sqlmodel import Session

from simple_db.database import engine
from simple_db.models.user import User

fake = Faker()


def create_realistic_email(name: str) -> str:
    """Generate realistic email variations from name"""
    parts = name.lower().split()
    first_name = parts[0].replace("'", "")
    last_name = parts[-1].replace("'", "") if len(parts) > 1 else ""

    # Different email format options
    email_formats = []

    if last_name:
        # first.last format
        email_formats.append(f"{first_name}.{last_name}")
        # firstlast format
        email_formats.append(f"{first_name}{last_name}")
        # first initial + last
        email_formats.append(f"{first_name[0]}{last_name}")
        # first + last initial
        email_formats.append(f"{first_name}.{last_name[0]}")
    else:
        email_formats.append(first_name)

    # Pick a random format
    base_email = random.choice(email_formats)

    # Randomly decide whether to add a number
    if random.choice([True, False, False]):  # 33% chance to add numbers
        base_email += str(random.randint(10, 999))

    # Select domain with weighted distribution
    domains = [
        "example.com",  # 30%
        "phantomail.org",
        "norealmail.co",
        "ghostinbox.io",
        "fakemailhub.in",
        "nowheremail.dev",
        "nullpost.ai",
    ]

    # Use weighted random choice: example.com gets 30%, others split 70%
    domain = random.choices(domains, weights=[30, 10, 10, 10, 10, 10, 10])[0]

    return f"{base_email}@{domain}"


def create_fake_users(session: Session, num_users: int = 20):
    users = []

    for _ in range(num_users):
        name = fake.unique.name()
        email = create_realistic_email(name)
        user = User(name=name, email=email)
        users.append(user)

    session.add_all(users)
    session.commit()

    print(f"✅ Inserted {num_users} fake users into database")


def main():
    with Session(engine) as session:
        create_fake_users(session, num_users=20)


if __name__ == "__main__":
    main()

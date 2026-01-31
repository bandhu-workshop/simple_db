import random

from faker import Faker
from sqlmodel import Session

from simple_db.database import engine
from simple_db.models.item import Item

fake = Faker()


def create_realistic_item_name():
    """Generate realistic item names"""
    adjectives = [
        "Vintage",
        "Modern",
        "Elegant",
        "Classic",
        "Premium",
        "Deluxe",
        "Professional",
    ]
    item_types = [
        "Notebook",
        "Pen",
        "Desk Lamp",
        "Chair",
        "Keyboard",
        "Monitor",
        "Headphones",
        "Mouse",
        "Charger",
        "Cable",
    ]

    adjective = random.choice(adjectives)
    item_type = random.choice(item_types)

    return adjective, item_type


# Base prices for each item type (close prices for same type)
BASE_PRICES = {
    "Notebook": 25.00,
    "Pen": 3.50,
    "Desk Lamp": 45.00,
    "Chair": 150.00,
    "Keyboard": 75.00,
    "Monitor": 250.00,
    "Headphones": 80.00,
    "Mouse": 25.00,
    "Charger": 20.00,
    "Cable": 10.00,
}

# Price multipliers mapped to adjectives (fixed price for each unique item)
PRICE_MULTIPLIERS = {
    "Vintage": 0.8,
    "Modern": 1.0,
    "Elegant": 1.2,
    "Classic": 1.1,
    "Premium": 1.5,
    "Deluxe": 1.7,
    "Professional": 1.9,
}

# Tax rates mapped to adjectives (as percentage of base price)
TAX_RATES = {
    "Vintage": 0.0,
    "Modern": 5.0,
    "Elegant": 10.0,
    "Classic": 12.0,
    "Premium": 15.0,
    "Deluxe": 18.0,
    "Professional": 20.0,
}


def create_fake_items(session: Session, num_items: int = 50):
    items = []

    for _ in range(num_items):
        adjective, item_type = create_realistic_item_name()
        name = f"{adjective} {item_type}"
        description = fake.sentence(nb_words=10)

        # Price is fixed for each unique item (adjective + type combination)
        base_price = BASE_PRICES[item_type]
        multiplier = PRICE_MULTIPLIERS[adjective]
        price = round(base_price * multiplier, 2)

        # Tax is percentage of price based on adjective
        tax_percentage = TAX_RATES[adjective]
        tax = round(price * (tax_percentage / 100), 2)

        on_offer = random.choice([True, False, False])  # 33% chance to be on offer

        item = Item(
            name=name, description=description, price=price, tax=tax, on_offer=on_offer
        )
        items.append(item)

    session.add_all(items)
    session.commit()

    print(f"✅ Inserted {num_items} fake items into database")


def main():
    with Session(engine) as session:
        create_fake_items(session, num_items=50)


if __name__ == "__main__":
    main()

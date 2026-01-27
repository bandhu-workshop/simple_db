import os

from sqlmodel import create_engine

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql+psycopg://admin:admin123@localhost:5432/fastapi_db"
)

engine = create_engine(DATABASE_URL, echo=True)

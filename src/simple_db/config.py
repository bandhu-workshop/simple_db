import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv(
        "POSTGRESS_URL", "postgresql+psycopg://admin:admin123@localhost:5432/fastapi_db"
    )
    DEBUG: bool = True


settings = Settings()

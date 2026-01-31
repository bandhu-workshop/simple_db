from contextlib import asynccontextmanager

from fastapi import FastAPI

from simple_db.api import items, users
from simple_db.database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create tables if they don't exist
    create_db_and_tables()
    yield
    # Shutdown: cleanup if needed


app = FastAPI(
    title="Simple DB API",
    description="A simple database API",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(items.router, prefix="/api/v1/items", tags=["items"])


@app.get("/health")
def health_check():
    return {"status": "ok"}

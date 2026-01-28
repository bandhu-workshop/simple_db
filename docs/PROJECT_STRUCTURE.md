# Simple DB - Project Structure & Architecture

## Table of Contents
1. [Overview](#overview)
2. [Folder Structure](#folder-structure)
3. [Core Components](#core-components)
4. [Design Patterns](#design-patterns)
5. [How to Run](#how-to-run)
6. [Adding New Features](#adding-new-features)

---

## Overview

This project follows **FastAPI best practices** with a clean, scalable, and maintainable architecture. The structure separates concerns into distinct layers:

- **API Layer** - Route handlers and request/response management
- **Service Layer** - Business logic
- **Model Layer** - Database ORM models
- **Schema Layer** - Pydantic validation models
- **Database Layer** - SQLAlchemy configuration and session management

---

## Folder Structure

```
simple_db/
├── src/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                 # FastAPI app initialization
│   │   ├── config.py               # Configuration & environment variables
│   │   ├── database.py             # Database connection & session management
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── users.py            # User routes (endpoints)
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── user.py             # Database models (SQLAlchemy ORM)
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   └── user.py             # Pydantic schemas (validation)
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── user_service.py     # Business logic layer
│   │   └── dependencies.py         # Shared dependencies (future)
│   └── run.py                      # Entry point - starts the server
├── tests/
│   ├── __init__.py
│   ├── test_users.py               # User endpoint tests
│   └── conftest.py                 # Pytest configuration & fixtures
├── docs/
│   ├── PROJECT_STRUCTURE.md        # This file
│   ├── API_DOCUMENTATION.md        # API endpoints documentation
│   └── DATABASE_DESIGN.md          # Database schema documentation
├── .env                            # Environment variables (local)
├── .env.example                    # Environment variables template
├── requirements.txt                # Python dependencies
├── .gitignore
├── README.md
└── pyproject.toml                  # Optional: Modern Python config
```

---

## Core Components

### 1. **Entry Point** (`src/run.py`)
- Starts the Uvicorn server
- Loads the FastAPI application from `app.main`
- Enables hot-reload in development mode

**Usage:**
```bash
python src/run.py
```

### 2. **Main Application** (`src/app/main.py`)
- Creates the FastAPI app instance
- Registers all route routers
- Configures metadata (title, description, version)
- Includes health check endpoint

### 3. **Configuration** (`src/app/config.py`)
- Manages environment variables using Pydantic Settings
- Loads values from `.env` file
- Single source of truth for app configuration

**Example:**
```python
from app.config import settings
db_url = settings.DATABASE_URL
```

### 4. **Database Layer** (`src/app/database.py`)
- Initializes SQLAlchemy engine
- Creates session factory
- Provides dependency injection function `get_db()`
- Defines Base class for all models

**Key Function:**
```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### 5. **API Layer** (`src/app/api/`)
- Contains all route handlers (routers)
- Each resource gets its own file (e.g., `users.py`, `products.py`)
- Routes are prefixed with `/api/v1/` for versioning
- Uses dependency injection for database access

**Example Endpoint:**
```python
@router.post("/", response_model=UserResponse)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)
```

### 6. **Models Layer** (`src/app/models/`)
- SQLAlchemy ORM models
- Represents database tables
- One file per model class
- Inherits from `Base` imported from `database.py`

**Example Model:**
```python
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
```

### 7. **Schemas Layer** (`src/app/schemas/`)
- Pydantic models for request/response validation
- Separate create, update, and response schemas
- Automatic API documentation generation
- Type hints for IDE support

**Example Schemas:**
```python
class UserCreate(BaseModel):
    email: EmailStr
    name: str

class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime
```

### 8. **Services Layer** (`src/app/services/`)
- Business logic separation
- Database queries and operations
- Reusable functions across endpoints
- Easier to test

**Example Service:**
```python
def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
```

---

## Design Patterns

### 1. **Dependency Injection**
FastAPI's `Depends()` is used throughout:
- Database session injection: `db: Session = Depends(get_db)`
- Promotes testability and loose coupling

### 2. **Separation of Concerns**
- **Routes** - Handle HTTP requests/responses
- **Services** - Contain business logic
- **Models** - Define database schema
- **Schemas** - Handle validation

### 3. **API Versioning**
Routes are prefixed with `/api/v1/`:
```python
app.include_router(users.router, prefix="/api/v1/users")
```
This allows easy migration to `/api/v2/` in the future.

### 4. **Configuration Management**
Environment variables are centralized in `config.py`:
- Load from `.env` file
- Type-safe with Pydantic
- Easy to override per environment

---

## How to Run

### Prerequisites
```bash
pip install -r requirements.txt
```

### Development Mode
```bash
cd /home/db/Work/simple_db
python src/run.py
```

The server will:
- Start on `http://localhost:8000`
- Enable hot-reload (auto-restart on file changes)
- Provide interactive API docs at `/docs`
- Provide ReDoc at `/redoc`

### Production Mode
```bash
cd src
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Available Endpoints
- `GET /health` - Health check
- `GET /api/v1/users` - List all users
- `POST /api/v1/users` - Create a new user
- `GET /docs` - Swagger UI
- `GET /redoc` - ReDoc documentation

---

## Adding New Features

### Example: Adding a Product Resource

#### 1. Create Model (`src/app/models/product.py`)
```python
from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
```

#### 2. Create Schemas (`src/app/schemas/product.py`)
```python
from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float

    class Config:
        from_attributes = True
```

#### 3. Create Service (`src/app/services/product_service.py`)
```python
from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate

def create_product(db: Session, product: ProductCreate):
    db_product = Product(name=product.name, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
```

#### 4. Create Routes (`src/app/api/products.py`)
```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.product import ProductCreate, ProductResponse
from app.services.product_service import create_product

router = APIRouter()

@router.post("/", response_model=ProductResponse)
def create_product_endpoint(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)
```

#### 5. Register in Main App (`src/app/main.py`)
```python
from app.api import products

app.include_router(products.router, prefix="/api/v1/products", tags=["products"])
```

---

## Best Practices Summary

✅ **Do:**
- Keep models, schemas, and services separate
- Use dependency injection for database access
- Validate input with Pydantic schemas
- Use async/await where applicable
- Write unit tests for services and endpoints
- Use meaningful variable and function names
- Document complex business logic

❌ **Don't:**
- Mix business logic with route handlers
- Create database queries in route functions
- Use hardcoded values (use `.env` instead)
- Skip input validation
- Create giant files (keep them focused)

---

## Environment Variables

Create a `.env` file based on `.env.example`:

```
DATABASE_URL=postgresql+psycopg://admin:admin123@localhost:5432/fastapi_db
DEBUG=True
```

For production:
```
DATABASE_URL=postgresql+psycopg://user:password@prod-host:5432/dbname
DEBUG=False
```

---

## Testing

Run tests with pytest:
```bash
pytest tests/
```

For coverage report:
```bash
pytest --cov=app tests/
```

---

## Further Reading

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/20/orm/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Python Async/Await](https://docs.python.org/3/library/asyncio.html)

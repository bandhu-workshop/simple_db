# Simple DB Project

This project is designed as a learning exercise to understand the basics of FastAPI, SQLModel, and Alembic. It provides a simple API for managing users and items, backed by a PostgreSQL database.

## Features
- RESTful API built with FastAPI
- Data models and ORM using SQLModel
- Database migrations managed with Alembic
- Example scripts to seed users and items
- Docker Compose setup for local development

## Project Structure
- `src/` - Main application code
  - `simple_db/` - Core package
    - `api/` - API route definitions
    - `models/` - Database models
    - `schemas/` - Pydantic schemas
    - `services/` - Business logic
    - `config.py` - Configuration
    - `database.py` - Database connection
    - `main.py` - FastAPI app entrypoint
- `scripts/` - Data seeding scripts
- `localdev/` - Local development resources (Postgres data, configs)
- `dockercompose.yml` - Docker Compose setup
- `pyproject.toml` - Project dependencies and settings
- `alembic/` - (if present) Alembic migration scripts

## Getting Started

### Prerequisites
- Python 3.10+
- Docker & Docker Compose (for local DB)

### Installation
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd simple_db
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
   Or, if using Poetry:
   ```sh
   poetry install
   ```
3. Start the database with Docker Compose:
   ```sh
   docker compose up -d
   ```
4. Run database migrations:
   ```sh
   alembic upgrade head
   ```
5. Start the FastAPI server:
   ```sh
   uvicorn src.simple_db.main:app --reload
   ```

### Seeding Data
To populate the database with example data:
```sh
python scripts/seed_users.py
python scripts/seed_items.py
```

### API Documentation
Once the server is running, access the interactive API docs at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Learning Goals
- Understand FastAPI basics: routing, dependency injection, async endpoints
- Use SQLModel for ORM and data validation
- Manage schema migrations with Alembic
- Structure a modern Python web API project

## References
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLModel Documentation](https://sqlmodel.tiangolo.com/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)

---

Feel free to explore the code, run the API, and experiment with the models and endpoints!

# Simple DB - Database Design

## Overview

The Simple DB uses PostgreSQL with SQLAlchemy ORM for Python object mapping.

---

## Tables

### Users Table

**Table Name:** `users`

**Purpose:** Store user information

**Columns:**

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | Integer | PRIMARY KEY, Auto-increment | Unique user identifier |
| `email` | String | UNIQUE, NOT NULL, INDEX | User email address |
| `name` | String | NOT NULL | User's full name |
| `created_at` | DateTime | NOT NULL, DEFAULT: NOW() | Account creation timestamp |

**SQL Definition:**
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR UNIQUE NOT NULL,
    name VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX ix_users_email ON users(email);
```

---

## Models

### User Model

**Location:** `src/app/models/user.py`

```python
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
```

**Usage in Services:**
```python
# Create
user = User(email="test@example.com", name="Test User")
db.add(user)
db.commit()

# Read
user = db.query(User).filter(User.email == "test@example.com").first()

# Update
user.name = "Updated Name"
db.commit()

# Delete
db.delete(user)
db.commit()
```

---

## Future Enhancements

### Relationships Example (for future features)

**If adding Products:**
```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    # ...existing columns...
    products = relationship("Product", back_populates="owner")

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="products")
```

---

## Database Migrations

For managing schema changes, use **Alembic**:

```bash
pip install alembic
alembic init migrations
alembic revision --autogenerate -m "Add users table"
alembic upgrade head
```

---

## Backup & Recovery

**PostgreSQL backup:**
```bash
pg_dump -U admin -d fastapi_db > backup.sql
```

**Restore from backup:**
```bash
psql -U admin -d fastapi_db < backup.sql
```

---

## Performance Considerations

- ✅ Index on `email` for faster lookups
- ✅ Use pagination for large result sets
- ✅ Consider connection pooling for production
- ✅ Use `select()` with specific columns to reduce memory
- ✅ Implement caching for frequently accessed data

---

## Connection Details

The database configuration is managed in `src/app/config.py`:

```python
DATABASE_URL: str = os.getenv(
    "DATABASE_URL", 
    "postgresql+psycopg://admin:admin123@localhost:5432/fastapi_db"
)
```

Update the connection string based on your environment.

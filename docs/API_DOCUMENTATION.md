# Simple DB - API Documentation

## Overview

The Simple DB API provides endpoints for managing users in the database.

**Base URL:** `http://localhost:8000`

**API Version:** `v1` (prefix: `/api/v1`)

---

## Endpoints

### Users Resource

#### 1. Get All Users
```
GET /api/v1/users
```

**Description:** Retrieve a list of all users from the database.

**Response:**
```json
[
  {
    "id": 1,
    "email": "user@example.com",
    "name": "John Doe",
    "created_at": "2026-01-28T10:30:00"
  }
]
```

**Status Codes:**
- `200` - Success

---

#### 2. Create User
```
POST /api/v1/users
```

**Description:** Create a new user.

**Request Body:**
```json
{
  "email": "newuser@example.com",
  "name": "Jane Doe"
}
```

**Response:**
```json
{
  "id": 2,
  "email": "newuser@example.com",
  "name": "Jane Doe",
  "created_at": "2026-01-28T11:00:00"
}
```

**Status Codes:**
- `200` - User created successfully
- `422` - Validation error (invalid email format)

---

### Health Check

#### Health Status
```
GET /health
```

**Description:** Check if the API is running.

**Response:**
```json
{
  "status": "ok"
}
```

**Status Codes:**
- `200` - API is running

---

## Authentication

Currently, the API has no authentication. In production, consider adding:
- JWT tokens
- API keys
- OAuth2

---

## Error Responses

All errors follow this format:

```json
{
  "detail": "Error message describing what went wrong"
}
```

**Common Status Codes:**
- `400` - Bad Request
- `422` - Validation Error
- `404` - Not Found
- `500` - Internal Server Error

---

## Usage Examples

### Using cURL

**List users:**
```bash
curl -X GET "http://localhost:8000/api/v1/users"
```

**Create user:**
```bash
curl -X POST "http://localhost:8000/api/v1/users" \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","name":"John Doe"}'
```

### Using Python requests

```python
import requests

# List users
response = requests.get("http://localhost:8000/api/v1/users")
print(response.json())

# Create user
payload = {
    "email": "newuser@example.com",
    "name": "Jane Doe"
}
response = requests.post("http://localhost:8000/api/v1/users", json=payload)
print(response.json())
```

---

## Interactive Documentation

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

Visit these URLs to explore and test endpoints interactively.

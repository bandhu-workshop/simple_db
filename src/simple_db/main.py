from fastapi import FastAPI

from simple_db.api import users

app = FastAPI(
    title="Simple DB API", description="A simple database API", version="1.0.0"
)

app.include_router(users.router, prefix="/api/v1/users", tags=["users"])


@app.get("/health")
def health_check():
    return {"status": "ok"}

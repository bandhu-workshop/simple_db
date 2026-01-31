# Postgress Docker Compose commands
pg-up:
	docker compose -f ./dockercompose.yml up -d
pg-down:
	docker compose -f ./dockercompose.yml down

# Format and type checking
check_format:
	@echo "Checking format..."
	uv run ruff@0.9.7 check && uv tool run ruff@0.9.7 format --check

check_type:
	@echo "Checking types..."
	uv run mypy --package db_learn

format:
	@echo "Formatting code..."
	uv tool run ruff@0.9.7 check --fix && uv tool run ruff@0.9.7 format

api:
	@echo "Starting API server..."
	uv run python -m uvicorn simple_db.main:app --host 0.0.0.0 --port=8080 --reload

seed_users:
	@echo "Seeding users into the database..."
	uv run python scripts/seed_users.py
# 	PYTHONPATH=src uv run python scripts/seed_users.py

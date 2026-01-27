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

# ==============================
# General Docker Commands
# ==============================

up:
	docker compose up

down:
	docker compose down

build:
	docker compose build

rebuild:
	docker compose down
	docker compose up --build

shell:
	docker exec -it verbalyst-api sh

psql:
	docker exec -it verbalyst_db psql -U verbalyst_user -d verbalyst_db


# ==============================
# Alembic Migrations
# ==============================

revision:
	docker compose exec backend alembic revision --autogenerate -m

migrate:
	docker compose exec backend alembic upgrade head

downgrade:
	docker compose exec backend alembic downgrade -1

history:
	docker compose exec backend alembic history

# ==============================
# Cleanup
# ==============================

clean:
	docker system prune -af --volumes

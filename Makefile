# ==============================
# General Docker Commands
# ==============================

up:
	docker compose up

down:
	docker compose down

build:
	docker compose build

front:
	docker compose stop nginx
	docker compose rm -f nginx
	docker rmi verbalyst-nginx || true
	docker compose build nginx
	docker compose up -d nginx

rebuild:
	docker compose down
	docker compose up --build

shell:
	docker exec -it verbalyst-api sh

psql:
	docker exec -it verbalyst_db psql -U verbalyst_user -d verbalyst_db

populate:
	docker compose exec backend python3 src/db/main.py



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

fix-alembic:
	sed -i 's/sqlmodel\.sql\.sqltypes\.AutoString()/sa.String()/g' backend/alembic/versions/*.py

# ==============================
# Cleanup
# ==============================

clean:
	docker system prune -af --volumes

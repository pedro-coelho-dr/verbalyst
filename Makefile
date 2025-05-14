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
# Backend Utilities
# ==============================

dev-server:
	docker compose exec backend uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

log:
	docker compose logs -f backend

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
# Database Checks
# ==============================

db-size:
	docker compose exec db psql -U verbalyst_user -d verbalyst_db -c "SELECT pg_size_pretty(pg_database_size(current_database())) AS total_size;"

table-counts:
	docker compose exec db psql -U verbalyst_user -d verbalyst_db -c "\
		SELECT 'profile' AS table, COUNT(*) FROM profile UNION ALL \
		SELECT 'word', COUNT(*) FROM word UNION ALL \
		SELECT 'room', COUNT(*) FROM room UNION ALL \
		SELECT 'game', COUNT(*) FROM game UNION ALL \
		SELECT 'player', COUNT(*) FROM player UNION ALL \
		SELECT 'guess', COUNT(*) FROM guess UNION ALL \
		SELECT 'distance', COUNT(*) FROM distance UNION ALL \
		SELECT 'hint', COUNT(*) FROM hint;"

# ==============================
# Cleanup
# ==============================

clean:
	docker system prune -af --volumes

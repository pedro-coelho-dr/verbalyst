## Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
gunicorn verb.api.routes:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```
backend/
.env
`CORS_ORIGINS=http://localhost:9000,http://localhost`

## Frontend
```bash
cd frontend/app
npm install -g @quasar/cli
npm install
quasar dev
```
frontend/app/
.env
```bash
#VITE_API_BASE_URL=http://localhost:8000/verb/
VITE_API_BASE_URL=http://localhost/verb/
```


## Root

```bash
docker compose build
docker compose up
docker compose down
docker compose up --build
```
backend
`docker exec -it verbalyst-api /bin/bash`

root/ 

`.env.template`

rename to `.env` 



docker exec -it verbalyst-api sh





docker compose exec backend python3 src/db/main.py

docker exec -it verbalyst_db psql -U verbalyst_user -d verbalyst_db


SELECT * FROM profile LIMIT 5;
SELECT * FROM word LIMIT 5;
SELECT * FROM room LIMIT 5;
SELECT * FROM game LIMIT 5;
SELECT * FROM player LIMIT 5;
SELECT * FROM guess LIMIT 5;
SELECT * FROM distance LIMIT 5;
SELECT * FROM hint LIMIT 5;




SELECT pg_size_pretty(pg_database_size(current_database())) AS total_database_size;

SELECT 
  relname AS table_name,
  pg_size_pretty(pg_total_relation_size(relid)) AS total_size
FROM pg_catalog.pg_statio_user_tables
ORDER BY pg_total_relation_size(relid) DESC;

SELECT 'profile' AS table, COUNT(*) FROM profile
UNION ALL SELECT 'word', COUNT(*) FROM word
UNION ALL SELECT 'room', COUNT(*) FROM room
UNION ALL SELECT 'game', COUNT(*) FROM game
UNION ALL SELECT 'player', COUNT(*) FROM player
UNION ALL SELECT 'guess', COUNT(*) FROM guess
UNION ALL SELECT 'distance', COUNT(*) FROM distance
UNION ALL SELECT 'hint', COUNT(*) FROM hint;

SELECT 
  relname AS table_name,
  n_live_tup AS estimated_rows,
  pg_size_pretty(pg_total_relation_size(relid)) AS total_size
FROM pg_stat_user_tables
ORDER BY pg_total_relation_size(relid) DESC;

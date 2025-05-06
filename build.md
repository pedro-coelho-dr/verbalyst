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


python -m app.scripts.create_db
python -m app.scripts.populate_words
python -m app.scripts.populate_games


docker exec -it verbalyst_db psql -U verbalyst_user -d verbalyst_db


\dt
\d word

SELECT * FROM word LIMIT 15;
SELECT COUNT(*) FROM word;
SELECT COUNT(DISTINCT word) FROM word;
SELECT word, COUNT(*) FROM word GROUP BY word HAVING COUNT(*) > 1;

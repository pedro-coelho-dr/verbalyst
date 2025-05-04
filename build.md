## Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
gunicorn verb.api.routes:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:9000
```
.env
`CORS_ORIGINS=http://localhost:9000,http://localhost

POSTGRES_DB=verbalyst_db
POSTGRES_USER=verbalyst_user
POSTGRES_PASSWORD=dev_secure_password_123
POSTGRES_HOST=db
POSTGRES_PORT=5432

DATABASE_URL=postgresql+psycopg2://verbalyst_user:dev_secure_password_123@db:5432/verbalyst_db`

## Frontend
```bash
cd frontend/app
npm install -g @quasar/cli
npm install
quasar dev
```

.env
`VITE_API_BASE_URL=http://localhost/verb/`


## Root

```bash
docker compose build
docker compose up
docker compose down
docker compose up --build
```
backend
`docker exec -it verbalyst-api /bin/bash`


.env
NGINX_ENV=dev
VITE_API_BASE_URL=http://localhost:8000
## Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
gunicorn verb.api.routes:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```
.env
`CORS_ORIGINS=http://localhost:9000,http://localhost`

## Frontend
```bash
cd frontend/app
npm install -g @quasar/cli
npm install
quasar dev
```

.env
`export VITE_API_BASE_URL=http://localhost/verb/`


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
`export NGINX_ENV=dev`
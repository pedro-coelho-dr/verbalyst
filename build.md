## Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
gunicorn verb.api.routes:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```
<<<<<<< HEAD
=======
backend/
>>>>>>> 140b4c4d08c51c1d06bdf9164f5f0191cfde269d
.env
`CORS_ORIGINS=http://localhost:9000,http://localhost`

## Frontend
```bash
cd frontend/app
npm install -g @quasar/cli
npm install
quasar dev
```
<<<<<<< HEAD

.env
`export VITE_API_BASE_URL=http://localhost/verb/`
=======
frontend/app/
.env
`VITE_API_BASE_URL=http://localhost/verb/`
>>>>>>> 140b4c4d08c51c1d06bdf9164f5f0191cfde269d


## Root

```bash
docker compose build
docker compose up
docker compose down
docker compose up --build
```
backend
`docker exec -it verbalyst-api /bin/bash`

<<<<<<< HEAD

.env
`export NGINX_ENV=dev`
=======
root/
.env
`NGINX_ENV=dev´
`VITE_API_BASE_URL=http://localhost/verb/`
>>>>>>> 140b4c4d08c51c1d06bdf9164f5f0191cfde269d

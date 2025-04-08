
# Quasar frontend builder

FROM node:22-alpine AS frontend-builder

WORKDIR /app
COPY ../frontend/app/ ./

ARG VITE_API_BASE_URL
ENV VITE_API_BASE_URL=${VITE_API_BASE_URL}

RUN npm install -g @quasar/cli
RUN npm install
RUN quasar build


# Nginx serving front-end

FROM nginx:alpine

ARG NGINX_ENV=dev

COPY ./nginx/${NGINX_ENV}.conf /etc/nginx/conf.d/default.conf

COPY --from=frontend-builder /app/dist/spa /usr/share/nginx/html



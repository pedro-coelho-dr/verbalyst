FROM node:22-alpine AS builder

WORKDIR /app

COPY ./app/ ./

RUN npm install
RUN npm run build

FROM node:22-alpine AS builder

WORKDIR /app

COPY ./app/ ./

ENV NODE_ENV=production

RUN npm install
RUN npm run build

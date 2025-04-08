FROM node:22-alpine AS builder

WORKDIR /app

COPY ./app/ ./

RUN npm install -g @quasar/cli

RUN npm install

ENV NODE_ENV=production

RUN npm run build

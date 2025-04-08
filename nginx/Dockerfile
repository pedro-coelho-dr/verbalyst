FROM nginx:alpine


COPY default.conf /etc/nginx/conf.d/default.conf


COPY --from=frontend-builder /app/dist/spa /usr/share/nginx/html

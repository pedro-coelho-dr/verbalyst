#!/bin/bash

set -e

echo "[INFO] Initializing database and tables..."
python -m app.scripts.create_db
echo "[INFO] Database initialized successfully."

#!/bin/bash

set -e

echo "[INFO] Populating static games..."
python -m app.scripts.populate_games
echo "[INFO] Static games populated successfully."

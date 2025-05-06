#!/bin/bash
set -e

echo "[INFO] Populating Word table from vocab..."
python -m app.scripts.populate_words
echo "[DONE] Word table populated successfully."

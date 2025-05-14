import os
import sys
from logging.config import fileConfig

# Add the src directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from alembic import context
from sqlmodel import SQLModel
from src.core.database import engine

# Import all models to register metadata
import src.models  # assumes __init__.py does the imports

# Alembic config
config = context.config
if config.config_file_name:
    fileConfig(config.config_file_name)

target_metadata = SQLModel.metadata

def run_migrations():
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )
        with context.begin_transaction():
            context.run_migrations()

run_migrations()

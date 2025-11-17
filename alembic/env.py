# alembic/env.py
import asyncio
from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import AsyncEngine

from alembic import context
import os

from app.core.config import settings
from app.core.database import Base
from app.models import user  # <-- Import all models here

# this is the Alembic Config object
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# For autogenerate
target_metadata = Base.metadata

def get_url():
    return settings.get_db_url()

async def run_migrations_online():
    connectable = AsyncEngine(
        sqlalchemy.engine.create_engine(
            get_url(),
            poolclass=pool.NullPool,
            future=True
        )
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()

def do_run_migrations(connection: Connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,
        compare_server_default=True
    )

    with context.begin_transaction():
        context.run_migrations()

asyncio.run(run_migrations_online())

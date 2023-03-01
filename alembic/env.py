import asyncio
from logging.config import fileConfig
from sqlite3 import Connection

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from sqlalchemy.ext.asyncio import async_engine_from_config

from app import system_config
from app.connect_db import Base
from app.models import User
import os
from dotenv import load_dotenv

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config
# this will overwrite the ini-file sqlalchemy.url path
# with the path given in the config of the main code
config.set_main_option("sqlalchemy.url",
                       f"postgresql+asyncpg://{system_config.db_user}:{system_config.db_password}@{system_config.host}:{system_config.post_port}/{system_config.db_db}")
# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from app import models

target_metadata = User.metadata


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""

    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

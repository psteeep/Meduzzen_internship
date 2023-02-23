from databases import Database
from app import system_config
import aioredis
from sqlalchemy.ext.declarative import declarative_base

URI = f"postgresql://{system_config.db_user}:{system_config.db_password}@postgres/{system_config.db_db}"

Base = declarative_base()


def get_db():
    db = Database(URI)
    return db


def get_redis():
    redis = aioredis.from_url("redis://redis")
    return redis

from databases import Database
from app import system_config
import aioredis

URI = f"postgresql://{system_config.db_user}:{system_config.db_password}@postgres/{system_config.db_db}"


def get_db():
    db = Database(URI)
    return db


def get_redis():
    redis = aioredis.from_url("redis://redis")
    return redis

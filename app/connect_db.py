from databases import Database
import system_config
import aioredis

URI = f"postgresql://{system_config.db_user}:{system_config.db_password}@postgres/{system_config.db_db}"

db = Database(URI)
redis = aioredis.from_url("redis://redis")


def get_db():
    return db


def get_redis():
    return redis

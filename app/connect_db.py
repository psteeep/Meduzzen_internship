from databases import Database
import system_config
import aioredis
from sqlalchemy.ext.declarative import declarative_base

URI = f"postgresql://{system_config.db_user}:{system_config.db_password}@{system_config.host}:{system_config.post_port}/{system_config.db_db}"

Base = declarative_base()
db = Database(URI)
redis = aioredis.from_url(system_config.redis)

def get_db():
    return db


def get_redis():
    return redis

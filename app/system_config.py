import os
from dotenv import load_dotenv

load_dotenv()

dev_port = int(os.getenv('DEV_PORT'))
host = os.getenv('HOST')
db_url = os.getenv("DATABASE_URL")
db_user = os.getenv("DATABASE_USER")
db_password = os.getenv("DATABASE_PASSWORD")
db_db = os.getenv("DATABASE_DB")

redis = os.getenve("REDIS_PORT")

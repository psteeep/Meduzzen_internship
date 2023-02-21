import os
from dotenv import load_dotenv

load_dotenv()

dev_port = int(os.getenv('DEV_PORT'))
host = os.getenv('HOST')

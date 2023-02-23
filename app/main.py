import uvicorn
from fastapi import FastAPI
from app import system_config
from app import connect_db
import os
from app.schemas.schemas import User as SchemaUser
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))
app = FastAPI()


@app.get("/")
async def health_check():
    return {
        "status_code": 200,
        "detail": "ok",
        "result": "working"
    }


@app.on_event("startup")
async def startup():
    redis = await connect_db.get_redis()
    db = connect_db.get_db()
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    db = connect_db.get_db()
    await db.disconnect()


@app.post("/user/", response_model=SchemaUser)
def create_user(user: SchemaUser):
    pass


if __name__ == '__main__':
    uvicorn.run('main:app', host=system_config.host, port=system_config.dev_port, reload=True)

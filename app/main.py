import uvicorn
from fastapi import FastAPI
import databases
from app import system_config
import asyncio
import aioredis

database = databases.Database(
    f"postgresql://{system_config.db_user}:{system_config.db_password}@postgres/{system_config.db_db}")

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
    redis = await aioredis.from_url("redis://redis")
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run('main:app', host=system_config.host, port=system_config.dev_port, reload=True)

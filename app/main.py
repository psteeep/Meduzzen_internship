import uvicorn
from fastapi import FastAPI
import system_config

app = FastAPI()


@app.get("/")
async def health_check():
    return {
        "status_code": 200,
        "detail": "ok",
        "result": "working"
    }

if __name__ == '__main__':
    uvicorn.run('main:app', host=system_config.host, port=system_config.dev_port, reload=True)

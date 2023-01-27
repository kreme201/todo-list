from fastapi import FastAPI

app = FastAPI()

from .routers import api_v1_router

app.include_router(api_v1_router)


@app.get("/")
def index():
    return {"message": "hello"}

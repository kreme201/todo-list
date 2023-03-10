from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routers import api_v1_router, view_router

app = FastAPI()
app.mount("/assets", StaticFiles(directory="app/assets"), name="assets")


app.include_router(api_v1_router)
app.include_router(view_router, include_in_schema=False)

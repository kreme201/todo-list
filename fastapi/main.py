from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import view
from routers.v1 import todo

app = FastAPI()

app.mount("/assets", StaticFiles(directory="assets"), name="assets")

app.include_router(view.router)
app.include_router(todo.router)

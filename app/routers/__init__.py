from fastapi import APIRouter

from .v1 import todo

api_v1_router = APIRouter(prefix="/api/v1")
api_v1_router.include_router(todo.router)

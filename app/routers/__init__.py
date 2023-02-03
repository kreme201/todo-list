from fastapi import APIRouter

from .v1 import todo
from .view import view_router

api_v1_router = APIRouter(prefix="/api/v1", tags=["TODO"])
api_v1_router.include_router(todo.router)

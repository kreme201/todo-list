from typing import List

from fastapi import APIRouter

router = APIRouter(prefix="/todo")

todo_items: List[str] = []


@router.get("/")
def get_todo_list():
    return todo_items


@router.post("/")
def create_todo_item(content: str):
    todo_items.append(content)

    return todo_items


@router.put("/{todo_id}")
def update_todo_item(todo_id: int, content: str):
    todo_items[todo_id] = content
    return todo_items


@router.delete("/{todo_id}")
def delete_todo_item(todo_id: int):
    del todo_items[todo_id]
    return todo_items

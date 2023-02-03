from dataclasses import dataclass
from datetime import datetime
from typing import Any, List, Union

from fastapi import APIRouter

router = APIRouter(prefix="/todo", tags=["TODO"])


class Todo:
    id: int
    status: bool
    content: str
    created: datetime

    def __init__(self, content: str):
        self.id = (
            max([item.id for item in todo_items]) if len(todo_items) > 0 else 0
        ) + 1
        self.status = False
        self.content = content
        self.created = datetime.now()


todo_items: List[Todo] = []


@router.get("/")
def get_todo_list() -> List[Todo]:
    return todo_items


@router.post("/")
def create_todo_item(content: str) -> Todo:
    new_item = Todo(content)
    todo_items.append(new_item)

    return new_item


@router.put("/{todo_id}")
def update_todo_item(
    todo_id: int,
    status: bool,
) -> Union[Todo, bool]:
    idx = [item.id for item in todo_items].index(todo_id)

    if idx >= 0:
        todo_items[idx].status = status

        return todo_items[idx]
    return False


@router.delete("/{todo_id}")
def delete_todo_item(todo_id: int) -> bool:
    idx = [item.id for item in todo_items].index(todo_id)
    if idx >= 0:
        del todo_items[idx]

        return True

    return False

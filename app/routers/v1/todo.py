from typing import List, Union

from fastapi import APIRouter, Depends

from app.domain.todo.dto import CreateTodoDto, UpdateTodoDto
from app.domain.todo.entity import Todo
from app.domain.todo.service import TodoService

router = APIRouter(prefix="/todo", tags=["TODO"])


@router.get("/")
def get_todo_list(
    todoService: TodoService = Depends(),
) -> List[Todo]:
    return todoService.search()


@router.post("/")
def create_todo_item(
    input: CreateTodoDto,
    todoService: TodoService = Depends(),
) -> Todo:
    return todoService.create(input)


@router.put("/{todo_id}")
def update_todo_item(
    input: UpdateTodoDto,
    todoService: TodoService = Depends(),
) -> Union[Todo, bool]:
    return todoService.update(input)


@router.delete("/{todo_id}")
def delete_todo_item(
    todo_id: int,
    todoService: TodoService = Depends(),
) -> bool:
    return todoService.delete(todo_id)

from typing import List

from fastapi import Depends

from .dto import CreateTodoDto, UpdateTodoDto
from .entity import Todo
from .repository import TodoRepository


class TodoService:
    def __init__(self, todoRepository: TodoRepository = Depends()):
        self.todoRepository = todoRepository

    def create(self, input: CreateTodoDto):
        return self.todoRepository.create(input)

    def update(self, input: UpdateTodoDto):
        return self.todoRepository.update(input)

    def delete(self, id: int):
        return self.todoRepository.delete(id)

    def search(self):
        return self.todoRepository.search()

    def get(self, id):
        data: List[Todo] = self.todoRepository.search()

        idx = [item.id for item in data].index(id)

        if idx >= 0:
            return data[idx]

        return None

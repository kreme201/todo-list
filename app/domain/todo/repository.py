from typing import List

from .dto import CreateTodoDto, UpdateTodoDto
from .entity import Todo


class TodoRepository:
    data: List[Todo] = []

    def __init__(self):
        pass

    def create(self, input: CreateTodoDto):
        new_item = Todo(
            id=max([item.id for item in self.data]) + 1 if len(self.data) > 0 else 1,
            content=input.content,
        )
        self.data.append(new_item)
        return new_item

    def udpate(self, input: UpdateTodoDto):
        idx = [item.id for item in self.data].index(input.id)

        if idx >= 0:
            self.data[idx].status = input.status

            return self.data[idx]
        return False

    def delete(self, id: int):
        idx = [item.id for item in self.data].index(id)
        if idx >= 0:
            del self.data[idx]

            return True

        return False

    def search(self):
        return self.data

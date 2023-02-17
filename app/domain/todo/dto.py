from pydantic import BaseModel


class CreateTodoDto(BaseModel):
    content: str


class UpdateTodoDto(BaseModel):
    id: int
    status: bool

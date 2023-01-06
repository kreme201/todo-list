from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/todo")


@router.get("/")
def read_todos():
    return {"action": "return todo list items"}


@router.post("/")
def create_todo():
    return {"action": "create todo item"}


@router.put("/{todo_id}")
def update_todo(todo_id: int):
    return {"action": "update todo item", "todo_id": todo_id}


@router.delete("/{todo_id}")
def delete_todo(todo_id: int):
    return {"action": "delete todo item", "todo_id": todo_id}

from fastapi import APIRouter, Path, HTTPException, status

from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()

todo_list = []


@todo_router.post("/todo")
def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully."}


@todo_router.get("/todo", response_model=TodoItems)
def retrieve_todos() -> dict:
    return {"todos": todo_list}


@todo_router.get("/todo/{todo_id}")
def get_single_todo(todo_id: int = Path(..., title="Id of todo to be retrieved")) -> dict:
    for td in todo_list:
        if td.id == todo_id:
            return {"todo": td}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="The todo with provided id does not exist"
    )


@todo_router.put("/todo/{todo_id}")
def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="todo Id to be updated")) -> dict:
    for todo in todo_list:
        if todo.id is todo_id:
            todo.item = todo_data.item
            return {"message": "Todo updated successfully."}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="The todo with provided id does not exist"
    )


@todo_router.delete("/todo/{todo_id}")
def delete_one_todo(todo_id: int) -> dict:
    for td in todo_list:
        if todo_id is td.id:
            todo_list.pop(todo_list.index(td))
            return {'message': "todo with given id deleted sucsessfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="The todo with provided id does not exist"
    )


@todo_router.delete("/todo/")
def delete_all() -> dict:
    todo_list.clear()
    return {'message': "all todos deleted"}

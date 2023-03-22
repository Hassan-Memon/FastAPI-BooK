from fastapi import APIRouter, Path, HTTPException, status, Request, Depends

from model import Todo, TodoItem, TodoItems

from fastapi.templating import Jinja2Templates

todo_router = APIRouter()

todo_list = []

templates = Jinja2Templates(directory="templates/")


@todo_router.post("/todo")
def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)):
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse('todo.html', {
        "request": request,
        "todos": todo_list
    })


@todo_router.get("/todo", response_model=TodoItems)
def retrieve_todos(request: Request):
    return templates.TemplateResponse('todo.html', {
        "request": request,
        "todos": todo_list
    })


@todo_router.get("/todo/{todo_id}")
def get_single_todo(request: Request, todo_id: int = Path(..., title="Id of todo to be retrieved")):
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse("todo.html", {
                "request": request,
                "todo": todo
            })

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

from fastapi import FastAPI
from todo import todo_router

app = FastAPI()

@app.get("/")
def welcome() -> dict:
    return {"message": "Assalamualikum from fastapi"}
    
app.include_router(todo_router)


from pydantic import BaseModel
from typing import List


class Todo(BaseModel):
    id: int
    item: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Example Schema!"
            }
        }


class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "read the next chapter please!"
            }
        }


# Response Model
class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example Schema 1"
                    },
                    {
                        "item": "Example Schema 2"
                    }
                ]
            }
        }

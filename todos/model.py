from fastapi import Form
from pydantic import BaseModel
from typing import List, Optional


class Todo(BaseModel):
    id: Optional[int]
    item: str

    @classmethod
    def as_form(
            cls, item: str = Form(...)
            ):
        return cls(item=item)

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

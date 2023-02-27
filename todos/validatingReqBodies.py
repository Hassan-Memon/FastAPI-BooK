from fastapi import FastAPI
from pydantic import BaseModel

class PacktBook(BaseModel):
    id: int
    Name: str
    Publisher: str
    Isbn: str



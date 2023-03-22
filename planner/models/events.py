# events.py: This file will contain the model definition for events operations.
from pydantic import BaseModel


class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: list[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com / image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event."
                               "Ensure to comewith yourown copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }

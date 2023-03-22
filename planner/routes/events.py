# events.py: This file will handle routing operations such as creating, updating,
# and deleting events.
from fastapi import APIRouter, Body, HTTPException, status
from models.events import Event

event_router = APIRouter(
    tags=["Events"]
)

events = []

@event_router.get("/", response_model=list[Event])
def retrieve_all_events() -> list[Event]:
    return events


@event_router.get("/{id}", response_model=Event)
def retrieve_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="The Event with supplied id does not exist"
    )
@event_router.post('/new')
def create_event(body: Event = Body(...)) -> dict:
    body.id = len(events) + 1
    events.append(body)
    return {
        "message": "Event added successfully!"
    }

@event_router.delete('/{id}')
def delete_one_event(id: int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return {
                "message": "Event removed successfully!"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="The Event with provided ID does not exist."
    )


@event_router.delete("/")
def delete_all_events() -> dict:
    events.clear()
    return {"message": 'All Events Deleted successfully'}
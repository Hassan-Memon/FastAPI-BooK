# events.py: This file will handle routing operations such as creating, updating,
# and deleting events.

from fastapi import APIRouter, Depends, HTTPException, Request, status
from database.connection import get_session
from models.events import Event, EventUpdate
from sqlmodel import select, delete

event_router = APIRouter(
    tags=["Events"]
)

events = []

@event_router.get("/", response_model=list[Event])
def retrieve_all_events(session=Depends(get_session)) -> list[Event]:
    statement = select(Event)
    events = session.exec(statement).all()
    return events


@event_router.get("/{id}", response_model=Event)
def retrieve_event(id: int, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="The Event with supplied id does not exist"
    )


@event_router.post('/new')
def create_event(new_event: Event, session=Depends(get_session)) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)

    return {
        "message": "Event added successfully!"
    }


@event_router.put("/edit/{id}", response_model=Event)
def update_event(id: int, new_data: EventUpdate, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        event_data = new_data.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event, key, value)
        session.add(event)
        session.commit()
        session.refresh(event)

        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="The Event with supplied id does not exist"
    )


@event_router.delete('/{id}')
def delete_one_event(id: int, session=Depends(get_session)) -> dict:
    event = session.get(Event, id)
    if event:
        session.delete(event)
        session.commit()

        return {
            "message": "Event removed successfully!"
        }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="The Event with provided ID does not exist."
    )


@event_router.delete("/")
def delete_all_events(session=Depends(get_session)) -> dict:
    statement = delete(Event)
    session.exec(statement)
    session.commit()
    return {"message": 'All Events Deleted successfully'}
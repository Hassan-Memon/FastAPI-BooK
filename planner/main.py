from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routes.users import user_router
from routes.events import event_router
from database.connection import conn

import uvicorn

app = FastAPI()

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")


@app.on_event("startup")
def on_startup():
    conn()


# @app.get('/')
# async def home():
#     return RedirectResponse(url="/events/")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

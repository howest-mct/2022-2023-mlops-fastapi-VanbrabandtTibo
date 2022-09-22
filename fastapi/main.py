from fastapi import FastAPI
import json
from routers import (
    bird_router as bird,
    user_router as user
)

from models import (
    bird_model,
    user_model
)

import database as db
db.start_db()

app = FastAPI()

app.include_router(bird.router)
app.include_router(user.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

from fastapi import FastAPI
from schemas.user import User
from schemas.bird import Bird

from routers import (
    bird_router as bird,
    user_router as user
)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

app.include_router(bird.router)
app.include_router(user.router)
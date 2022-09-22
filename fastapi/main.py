from fastapi import FastAPI
import json
from schemas.bird import Bird
from schemas.user import User


app = FastAPI()

users = [
    {
        "name": "Nathan Segers",
        "locationOfResidence": "Aalst",
        "age": 24,
        "gender": "M",
        "registrationDate": "2022-09-22 12:00:00"
    }
]

with open('../birds.json', 'r') as f:
  birds = json.load(f)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/birds")
def getBirds():
    return birds

@app.get("/birds/{bird_id}")
async def getBird(bird_id):
    return list(filter(lambda bird: Bird(**bird).id == bird_id, birds)) # Filter the list of birds, and only return the bird we need.

@app.get("/users")
def getUsers():
    return users

@app.post("/user")
def postUser(user: User):
  users.append(user)
  return users
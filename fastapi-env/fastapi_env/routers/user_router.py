from fastapi import FastAPI, APIRouter

import json
from schemas.user import User

router = APIRouter(
    prefix="/users",
    tags=["User"],
    responses={404: {"User": "Not found"}},
)

users = [User(uuid="123456", name="Tibo", locationOfResidence="Tuttegemstraat 98", age="20", gender="male", registrationDate='08/08/2022')]

@router.get("/")
async def get_users():
    return users

@router.post("/add")
async def create_user(user: User):
    users.append(user)
    return users
from fastapi import APIRouter
from schemas.user import User

router = APIRouter(
    prefix="/users",
    tags=["User"],
    responses={404: {"User": "Not found"}},
)

users = [
    {
        "name": "Nathan Segers",
        "locationOfResidence": "Aalst",
        "age": 24,
        "gender": "M",
        "registrationDate": "2022-09-22 12:00:00"
    }
]

@router.get("/")
def getUsers():
    return users

@router.post("/")
def postUser(user: User):
  users.append(user)
  return users
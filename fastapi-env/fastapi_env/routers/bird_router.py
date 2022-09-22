from fastapi import FastAPI, APIRouter

import json
from schemas.bird import Bird

router = APIRouter(
    prefix="/birds",
    tags=["Bird"],
    responses={404: {"Bird": "Not found"}},
)

f = open('D://3MCT//MLOps//LAB1//2022-2023-mlops-fastapi-VanbrabandtTibo//birds.json')
birds = json.load(f)

@router.get("/")
async def get_birds():
    return birds

@router.get("/{id}")
async def get_bird(id: str):
    for bird in birds:
        if bird.id == id:
            return bird
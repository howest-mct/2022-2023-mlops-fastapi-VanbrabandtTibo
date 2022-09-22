from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    uuid: Optional[str]
    id: str
    name: str
    locationOfResidence: str
    age: int
    gender: str
    registrationDate: datetime

    class Config:
        orm_mode = True

    def sayHello(self):
        print("Hello, I am " + self.name)
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    uuid: Optional[str]
    name: str
    locationOfResidence: str
    age: str
    gender: str
    registrationDate: str
    def sayHello(self):
        pass
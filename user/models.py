from pydantic import BaseModel

class User(BaseModel):
    id: int = None
    name: str = "black"
    age: int = None
    mail: str = None
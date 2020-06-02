from pydantic import BaseModel

class User(BaseModel):
    id: int = None
    name: str = "example"
    age: int = None
    mail: str = None
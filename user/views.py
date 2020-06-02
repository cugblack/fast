from routers import router
from . import models

@router.post("/users/", tags=["users"])
async def users(user: models.User):
    """
    {
        "id": 1,
        "mail": "example@gmail.com",
        "age": 20,
        "name": "example"
    }	
    """
    return {"username": user.name, "age": user.age, "mail": user.mail}
 
@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}
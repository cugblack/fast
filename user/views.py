from routers import router
from . import models

@router.get("/users/", tags=["users"])
async def users(user: models.User):
    """
    {
        "id": 1,
        "mail": "test@gmail.com",
        "age": 20,
        "name": "oneplus"
    }	
    """
    return [{"username": user.name}, {"age": user.age}, {"mail": "test@gamil.com"}]
 
@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}
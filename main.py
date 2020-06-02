# """
# http://127.0.0.1:8080/docs
# http://127.0.0.1:8080/redoc
# """
# from fastapi import FastAPI
# from pydantic import BaseModel
# app = FastAPI()

# class People(BaseModel):
#     name: str
#     age: int
#     address: str
#     salary: float

    
# @app.get("/")
# def hello():
#     return {"Hello": "World"}

# @app.post('/user')
# def insert(people: People):
#     """
#     {
#         "name": "black",
#         "age": 20,
#         "address": "oneplus",
#         "salary": 200.18
#     }
#     """
#     age_after_10_years = people.age + 10
#     msg = f'此人名字叫做：{people.name}，十年后此人年龄：{age_after_10_years}'
#     return {'success': True, 'msg': msg}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None, p: str = None):
#     return {"item_id": item_id, "q": q, "p": p}


"""
启动操作 : d:\Python37\python.exe -m uvicorn main:app --host 127.0.0.1 --port 30080 --reload

docs     :   http://127.0.0.1:30080/docs
redoc    :   http://127.0.0.1:30080/redoc    
"""

from fastapi import FastAPI
from pydantic import BaseModel
import routers

def create_app():
    app = FastAPI()
    app.include_router(routers.router, prefix="/api")
    return app

app = create_app()
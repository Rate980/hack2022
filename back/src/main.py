import re

from fastapi import FastAPI, Response
from pydantic import BaseModel
from starlette.exceptions import HTTPException

from db import session
from model import TestUser, TestUserTable

app = FastAPI()


@app.get("/ping")
def root() -> str:
    return "pong"


@app.get("/users", response_model=list[TestUser])
def users() -> list[TestUser]:
    users = session.query(TestUserTable).all()
    # return [TestUser.from_orm(x) for x in users]
    return users


class UserData(BaseModel):
    name: str


@app.post("/users", status_code=201, response_model=TestUser)
def create_user(user: UserData) -> TestUser:
    check = session.query(TestUserTable).filter(TestUserTable.name == user.name).first()
    if check is not None:
        raise HTTPException(status_code=401, detail="user name")

    if re.match(r"^[0-9a-zA-Z]+$", user.name) is None:
        raise HTTPException(status_code=401, detail="user name")
    session.add(TestUserTable(name=user.name))
    session.commit()
    add_user = (
        session.query(TestUserTable).filter(TestUserTable.name == user.name).first()
    )
    return add_user


@app.get("/users/{user_name}", response_model=TestUser)
def get_user(user_name: str) -> TestUser:
    user = session.query(TestUserTable).filter(TestUserTable.name == user_name).first()
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")

    return user


class PatchUser(BaseModel):
    point: int


@app.patch("/users/{user_name}", response_model=TestUser)
def edit_user(user_name: str, user_data: PatchUser) -> TestUser:
    user = session.query(TestUserTable).filter(TestUserTable.name == user_name).first()
    user.point = user_data.point
    session.commit()
    return user


@app.delete("/users/{user_name}", response_model=TestUser)
def delete_user(user_name: str) -> Response:
    user = session.query(TestUserTable).filter(TestUserTable.name == user_name).first()
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")
    session.delete(user)
    session.commit()
    return Response(status_code=204)

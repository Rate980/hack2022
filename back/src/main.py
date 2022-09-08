import re
from audioop import add
from typing import Any, Optional

from fastapi import FastAPI, Response
from pydantic import BaseModel
from starlette.exceptions import HTTPException

from db import session
from model import TestUser, TestUserTable

app = FastAPI()


@app.get("/")
def root() -> Any:
    return {"message": "Hello World"}


@app.get("/users")
def users() -> Any:
    users = session.query(TestUserTable).all()
    return users


class UserData(BaseModel):
    name: str


@app.post("/users")
def create_user(user: UserData) -> Any:
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


@app.get("/users/{user_name}")
def get_user(user_name: str) -> Any:
    user = session.query(TestUserTable).filter(TestUserTable.name == user_name).first()
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return user


class PatchUser(BaseModel):
    point: int


@app.patch("/users/{user_name}")
def edit_user(user_name: str, user_data: PatchUser) -> Any:
    user = session.query(TestUserTable).filter(TestUserTable.name == user_name)
    user.point = user_data.point
    session.commit()
    return None


@app.delete("/users/{user_name}")
def delete_user(user_name: str) -> Any:
    user = session.query(TestUserTable).filter(TestUserTable.name == user_name).first()
    session.delete(user)
    return Response(status_code=204)

import hashlib
import json
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.exceptions import HTTPException

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/users")
def users():
    return


class UserData(BaseModel):
    name: str
    passwd: str
    email: str


@app.post("/users")
def create_user(user: UserData):
    pass


@app.get("/users/{user_name}")
def get_user(user_name: str):
    # user = data["users"].get(user_name)
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return user

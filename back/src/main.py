import hashlib
import json
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.exceptions import HTTPException

app = FastAPI()
jsonpath = Path(__file__).resolve().parent.joinpath("data.json")
with jsonpath.open(encoding="utf8") as f:
    data = json.load(f)


def dump():
    with jsonpath.open(encoding="utf8") as f:
        json.dump(data, f)


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/users")
def users():
    return [{"name": x["naem"], "point": x["point"]} for x in data["users"]]


class UserData(BaseModel):
    name: str
    passwd: str
    email: str


@app.post("/users")
def create_user(user: UserData):
    user_dict = user.dict()
    passwd = user.passwd
    user_dict["passwd"] = hashlib.sha256(passwd.encode("utf8"))


@app.get("/users/{user_name}")
def get_user(user_name: str):
    user = data["users"].get(user_name)
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return user

from fastapi import APIRouter
from .controllers import createUser, UserModel
from ..models.users import User
from pydantic import BaseModel


class UserModel(BaseModel):
    name: str


router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Foo"}, {"username": "Bar"}]


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    if username == "me":
        return {"username": username}
    return {"username": None}


@router.post("/users/", tags=["users"])
async def create_user(user: UserModel):
    r = await User.create(nickname=user.name)
    return {"response": r}


def init_app(app):
    app.include_router(router)

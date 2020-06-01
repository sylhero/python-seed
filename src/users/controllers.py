from ..models.users import User
from pydantic import BaseModel


class UserModel(BaseModel):
    name: str


async def createUser(user: UserModel):

    return User.create(nickname=user.name)

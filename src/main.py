from fastapi import FastAPI
import asyncio
from fastapi.middleware.cors import CORSMiddleware
from . import users
from . import items
from .db import DBInstance
from configparser import ConfigParser
# from ConfigParser import ConfigParser # for python3
data_file = 'config.ini'

config = ConfigParser()
config.read(data_file)

print(config["db"]["host"])
app = FastAPI()
# global instance
db = DBInstance.get_db_instance()
app.add_middleware(CORSMiddleware, allow_methods=["*"], allow_headers=["*"])


@app.on_event("startup")
async def startup():
    app.include_router(users.__init__())
    app.include_router(items.__init__())
    await db.set_bind(
        "postgresql://postgres:mysecretpassword@localhost:5432/auth")
    await db.gino.create_all()


@app.on_event("shutdown")
async def shutdown():
    await db.pop_bind().close()

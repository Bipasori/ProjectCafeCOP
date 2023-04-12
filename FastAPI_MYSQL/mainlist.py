from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from typing import List
from starlette.middleware.cors import CORSMiddleware

from db import session
from model import UserTable, User

import json

templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "/users 에서 사용자관리"}


# ----------API 정의------------
@app.get("/users", response_class=HTMLResponse)
async def read_users(request: Request):
    print("read_users >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    context = {}

    users = session.query(UserTable).all()

    context['request'] = request
    context['users'] = users

    return templates.TemplateResponse("user_list.html", context)


@app.get("/users/{user_id}", response_class=HTMLResponse)
async def read_user(request: Request, user_id: int):
    print("read_user >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    context = {}

    user = session.query(UserTable).filter(UserTable.id == user_id).first()
    print(user.name)
    context['name'] = user.name
    context['age'] = user.age
    context['request'] = request

    return templates.TemplateResponse("user_detail.html", context)


@app.post("/users")
async def create_user(users: User):
    print("create_user >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # data = await request.json()

    userlist = list(users)
    uname = userlist[1][1]
    uage = userlist[2][1]

    user = UserTable()
    user.name = uname
    user.age = uage

    session.add(user)
    session.commit()

    return { 'result_msg': f'{uname} Registered...' }


@app.put("/users")
async def modify_users(users: User):
    print("modify_user >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    userlist = list(users)
    uid = userlist[0][1]
    uname = userlist[1][1]
    uage = userlist[2][1]

    user = session.query(UserTable).filter(UserTable.id == uid).first()
    user.name = uname
    user.age = uage
    session.commit()

    return { 'result_msg': f"{uname} updated..." }


@app.delete("/users")
async def delete_users(users: User):
    print("delete_user >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    userlist = list(users)
    uid = userlist[0][1]

    user = session.query(UserTable).filter(UserTable.id == uid).delete()
    session.commit()

    return {'result_msg': f"User deleted..."}

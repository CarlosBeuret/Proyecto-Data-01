from fastapi import APIRouter, Body, Path, Query
from config.db import conn_mysql
from models.users import users
from schemas.user import User
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
user = APIRouter()


@user.get('/get_users/', tags=['User'])
def get_users():
    result = conn_mysql.execute((users.select()))
    
    columns = result.keys()
    users_list = [dict(zip(columns, row)) for row in result.fetchall()]
    return users_list

@user.get('/get_user/', tags=['User'])
def get_user(id: int):
    return conn_mysql.execute(users.select().where(users.c.id == id))


@user.post('/create_users/', tags=['User'])
def create_users(user: User):
    new_user = {"name": user.name, "email": user.email}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conn_mysql.execute(users.insert().values(new_user))
    conn_mysql.commit()
    print(result)
    return "Created"


@user.delete('/delete_user/', tags=['User'])
def delete_user(id: str):
    conn_mysql.execute(users.delete().where(users.c.id == id))
    conn_mysql.commit()
    return "Deleted"


@user.put('/update_user/', tags=['User'])
def update_user(id: str, user: User):
    conn_mysql.execute(users.update().values(
    name=user.name, email=user.email, 
    password=f.encrypt(user.password.encode("utf-8"))).where(users.c.id == id))
    conn_mysql.commit()
    return "Updated"

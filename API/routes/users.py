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
    return conn_mysql.execute((users.select())).fetchall()

@user.post('/create_users/', tags=['User'])
def create_users(user: User):
    new_user ={"name":user.name, "email": user.email}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conn_mysql.execute(users.insert().values(new_user)) 
    return conn_mysql.execute(users.select().where(users.c.id == result.lastrowid)).first()


    return conn_mysql.execute((users.select()).fetch_all())

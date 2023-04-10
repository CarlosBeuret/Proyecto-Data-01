from fastapi import APIRouter, Body, Path, Query
from config.db import conn_mysql
from models.users import users
from schemas.user import User
from cryptography.fernet import Fernet

user = APIRouter()


@user.get('/get_users/', tags=['User'])
def get_users():
    return conn_mysql.execute((users.select()).fetch_all())

@user.post('/create_users/', tags=['User'])
def create_users(user: User):
    new_user ={"name":user.name, "email": user.email}
    new_user

    return conn_mysql.execute((users.select()).fetch_all())

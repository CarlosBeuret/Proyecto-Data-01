from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine_mysql, meta

users = Table('users', meta, Column("id", Integer, prymary_key=True), Column(
    'name', String(255)), Column('mail', String(255)), Column('password', String(255)))

meta.create_all(engine_mysql)
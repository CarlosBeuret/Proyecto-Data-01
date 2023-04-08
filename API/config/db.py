
from sqlalchemy import create_engine, MetaData

Database_URL ="sqlite:///../Database/database.db"
engine = create_engine(url=Database_URL)

conn = engine.connect()

mysql_URL ="mysql+pymysql://root:root@localhost:3306/users"
engine_mysql = create_engine(url=mysql_URL)

conn_mysql = engine_mysql.connect()

# crea una instancia de MetaData
meta = MetaData()

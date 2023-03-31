
from sqlalchemy import create_engine, MetaData

# Definimos engine para la conexión con la base de datos.

Database_URL ="sqlite:///../Database/Database.db"
engine = create_engine(url=Database_URL)

conn = engine.connect()

# crea una instancia de MetaData
meta = MetaData()
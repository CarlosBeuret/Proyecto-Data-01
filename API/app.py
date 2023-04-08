# Importamos librerias

from fastapi import FastAPI
from routes.movies import movies
from routes.users import user

# Definimos la app.
app = FastAPI(
    title="Explorador de plataformas de stream",
    description="Permite buscar titulos de peliculas y filtrarlas",
    version="2.0.1",
)

app.include_router(movies)
app.include_router(user)















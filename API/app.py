# Importamos librerias

from fastapi import FastAPI,  APIRouter
from routes.movies import movies






# Definimos la app.
app = FastAPI(
    title="Explorador de plataformas de stream",
    description="Permite buscar titulos de peliculas y filtrarlas",
    version="2.0.1",
)

app.include_router(movies)
















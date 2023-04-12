from fastapi import APIRouter, Body, Path, Query
from fastapi.responses import JSONResponse
from config.db import engine, conn
import pandas as pd
from sqlalchemy import MetaData, Table, Column, update, String, Integer, create_engine
#from schemas.movies import Movies

movies = APIRouter()

# Metodos get


@movies.get('/max_duration/', tags=['Movies'])
def get_max_duration(platform: str , type_duration: str, year: int = Query(ge=1900,le=2030)):

    df = pd.read_sql("Database", con=engine)
    mascara = (df["release_year"] == year) & (df["platform"] ==
                                              platform) & (df["type_duration"] == type_duration)
    indice = df.loc[mascara]['duration'].idxmax()
    respuesta =df.loc[indice, 'title']
    return  JSONResponse(content= respuesta)


@movies.get('/count_platform/', tags=['Platform'])
def get_count_plataform(platforma: str):

    df = pd.read_sql("Database", con=engine)

    mascara = (df["platform"] == platforma)
    respuesta2 = df[mascara]['title'].groupby(by=df['type'])
    respuesta = respuesta2.aggregate('count').to_dict()
    return JSONResponse(content= respuesta)


@movies.get('/listedin/', tags=['Platform'])
def get_listedin(listed: str):
    listed = '%' + listed + '%'
    df = pd.read_sql(
        f'SELECT count(title) as cantidad, platform FROM Database WHERE  listed_in LIKE "{listed}"     GROUP BY platform ORDER BY cantidad  desc limit 1 ;', con=engine)
    df = df.to_dict('list')

    return  df


@movies.get('/actor/', tags=['Actor'])
def get_actor(plataforma: str, anio: int):
    df = pd.read_sql(
        f'SELECT *  FROM Database WHERE  platform = "{plataforma}"  and release_year = {anio};', con=engine)
    var_aux = (df['cast'].str.split(pat=',', expand=True))
    lista = [var_aux[j] for j in range(len(var_aux.columns))]
    var_aux2 = pd.concat(lista)
    var_aux2 = var_aux2.str.strip()
    var_aux2 = var_aux2.value_counts()
    var_aux3 = var_aux2.idxmax()
    var_aux4 = int(var_aux2[var_aux3])
    return var_aux3, var_aux4

@movies.post('/agregar_pelicula/', tags=['Movies'], status_code=201)
def create_movie(type: object = Body(), title: object = Body(),
                director: object = Body(), cast: object = Body(), 
                country: object = Body(), date_added: object = Body(), 
                release_year: int = Body(), rating: object = Body(), 
                genre: object = Body(), description: object = Body(),
                platform: object = Body(), duration: float = Body(), 
                type_duration: object = Body()):

    dic_movie = {'type': type, 'title': title, 'director': director, 'cast': cast, 'country': country, 'date_added': date_added, 'release_year': release_year,
                 'rating': rating, 'genre': genre, 'description': description, 'platform': platform, 'duration': duration, 'type_duration': type_duration}
    df = pd.DataFrame(dic_movie, index=[0])
    df.head()
    df.to_sql('Database', con=engine, if_exists='append', index=False)
   
    return JSONResponse(status_code= 201, content= f"La pelicula '{title}' fue agrdada con exito")


"""
# Metodo put


@movies.put('/modificar_titulo/', tags=['Movies'])
def update_movie(duration:float, title:str):
    query = f'UPDATE movies SET duration="{duration}" WHERE title={title}'
    conn.execute(query)
    return title

"""


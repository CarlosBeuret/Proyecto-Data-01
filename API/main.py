from fastapi import FastAPI
import  sqlalchemy as sql
import pandas as pd

app = FastAPI(
    title="Explorador de plataformas de stream",
    description="Permite buscar titulos de peliculas y filtrarlas",
    version="1.0.1",
)

Database_URL ="sqlite:///../Database/Database.db"
engine = sql.create_engine(url=Database_URL)


@app.get('/max_duration/' )
def get_max_duration(platform:str, type_duration:str, year:int):
    
    df= pd.read_sql("Database", con=engine)
    mascara = (df["release_year"]== year) & (df["platform"] == platform) & (df["type_duration"]== type_duration)
    indice = df.loc[mascara]['duration'].idxmax()
    return df.loc[indice,'title']

@app.get('/count_plataform/')
def get_count_plataform(platforma : str ):
  
    df= pd.read_sql("Database", con=engine)
   
    mascara = (df["platform"]== platforma) 
    respuesta2 =  df[mascara]['title'].groupby(by = df['type'])
   
    return respuesta2.aggregate('count').to_dict()

@app.get('/listedin/')
def get_listedin(listed : str ):
    listed = '%'+ listed +'%'
    df = pd.read_sql(f'SELECT count(title) as cantidad, platform FROM Database WHERE  listed_in LIKE "{listed}"     GROUP BY platform ORDER BY cantidad  desc limit 1 ;', con=engine)
    df = df.to_dict('list')
 
    return df


@app.get('/actor/')
def get_actor(plataforma : str, anio: int ):
    df = pd.read_sql(f'SELECT *  FROM Database WHERE  platform = "{plataforma}"  and release_year = {anio};', con=engine)   
    var_aux = (df['cast'].str.split(pat= ',',expand= True))
    lista = [var_aux[j] for j in range( len(var_aux.columns))]
    var_aux2 = pd.concat(lista)
    var_aux2= var_aux2.str.strip()
    var_aux2 = var_aux2.value_counts()
    var_aux3 = var_aux2.idxmax()
    var_aux4 = int(var_aux2[var_aux3])
    return var_aux3, var_aux4

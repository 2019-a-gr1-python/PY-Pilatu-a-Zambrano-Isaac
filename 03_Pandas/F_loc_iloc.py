import pandas as pd
import numpy as np
path_general='PYTHON_PROJECTS/PY-Pilatu-a-Zambrano-Isaac/03_Pandas/'
path_guardado=path_general+'data/csv/artwork_data.pickle'
df=pd.read_pickle(path_guardado)

primero = df.loc[1035,'artist']
primero

df.loc[0] #Error debido a que no existe este indice

primero_a=df.iloc[0,0]
primero_a


#Dataframe obteniendo los cien primeros artistas
#Con las dos primeras columnas
primero_c=df.iloc[0:100,0:2]



mayor_ancho=df.sort_values('width',ascending=0)[3:].head(3)
menor_ancho=df.sort_values('width',ascending=0)[3:].tail(3)

serie_width_validada=pd.to_numeric(df['width'],errors='coerce')

df.loc[:,'width']=serie_width_validada

serie_height_validada=pd.to_numeric(df['height'],errors='coerce')
df.loc[:,'height']=serie_height_validada

diez_primeros=df.sort_values('width',ascending=0).head(10)

diez_ultimas=df.sort_values('width',ascending=0).tail(10)


area=df['width']*df['height']
type(area)

df['area']=0
df['area']=area

id_max_area=df['area'].idxmax()
id_min_area=df['area'].idxmin()

registro_mayor_area=df.loc(id_max_area)
registro_menor_area=df.loc(id_min_area)

mayor_area=df.sort_values('area',ascending=0).head(1)
min_area=df.sort_values('area',ascending=0).tail(1)



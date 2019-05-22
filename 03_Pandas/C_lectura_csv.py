import pandas as pd
import os
path_general='PYTHON_PROJECTS/PY-Pilatu-a-Zambrano-Isaac/03_Pandas/'
path=path_general+'data/csv/artwork_data.csv'
df=pd.read_csv(
        path,
        nrows=50,
        usecols=['id','artist']
        )

columnas_a_usar=['id','artist','title','medium','year','acquisitionYear','height','units']

df_completo=pd.read_csv(
        path,
        usecols=columnas_a_usar,
        index_col='id'
        )

path_guardado=path_general+'data/csv/artwork_data.pickle'

df_completo.to_pickle(path_guardado)

df_completo_pickle=pd.read_pickle(path_guardado)
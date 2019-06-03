import pandas as pd
import numpy as np
path_general='PYTHON_PROJECTS/PY-Pilatu-a-Zambrano-Isaac/03_Pandas/'
path_guardado=path_general+'data/csv/artwork_data.pickle'
df_completo_pickle=pd.read_pickle(path_guardado)

serie_artistas_duplicados = df_completo_pickle['artist']
artistas = pd.unique(serie_artistas_duplicados)
artistas.size

len(artistas)

blake=df_completo_pickle['artist']=='Blake, William'
blake
df_blake=df_completo_pickle[blake]
type(df_blake)

import pandas as pd
import os
import json
path_general='PYTHON_PROJECTS/PY-Pilatu-a-Zambrano-Isaac/03_Pandas/data/artwork'
filename='/a/000/a00001-1035.json'
pd.read_json

path_archivo=path_general+filename

llaves=['id','all_artists','medium','dateText','acquisitionYear','height','width','units']

with open(path_archivo) as texto_json:
    contenido_json=json.load(texto_json)
    print(contenido_json)
    registro_df=[]
    for key in llaves:
        valor=contenido_json[key]
        registro_df.append(valor)

serie=tuple(registro_df)
    
df_small=pd.DataFrame(
        [registro_df]
        )

df_small_2=pd.DataFrame(
        [serie]
        )


def leer_json(path,llaves):
    with open(path_archivo) as texto_json:
        contenido_json=json.load(texto_json)
    registro_df_lista=[]
    for key in llaves:
        valor=contenido_json[key]
        registro_df.append(valor)
    return registro_df_lista

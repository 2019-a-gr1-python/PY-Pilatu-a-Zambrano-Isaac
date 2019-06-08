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


def leer_json(path_archivo,llaves):
    with open(path_archivo) as texto_json:
        contenido_json = json.load(texto_json)
    registro_df_lista = []
    for llave in llaves:
        valor = contenido_json[llave]
        registro_df_lista.append(valor)
    return registro_df_lista

def leer_json_en_carpetas(directorio, llaves):
    trabajos_arte=[]
    for path_raiz, lista_directorios, archivos in os.walk(directorio):
               
        for nombre_archivo in archivos:
            if (nombre_archivo.endswith('json')):
                directorio_archivo=os.path.join(path_raiz,nombre_archivo)
                pieza_arte = leer_json(directorio_archivo,llaves)
                print(directorio_archivo)
                trabajos_arte.append(pieza_arte)
                
    df=pd.DataFrame.from_records(
            trabajos_arte,
            columns=llaves,
            index='id'
            )
    return df

df_artworks=leer_json_en_carpetas(path_general,llaves)



    

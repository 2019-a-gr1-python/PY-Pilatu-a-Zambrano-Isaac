import pandas as pd
import os
import json
import matplotlib.pyplot as plt

#OBJETIVOS
#TOP CAUSAS DE MUERTE
#RELACION ENTRE SEXO Y SUICIDIO
#RELACION ENTRE ESTADO MARITAL Y SUICIDIO
#RELACION ENTRE SEXO, ESTADO MARITAL Y SUICIDIO
#RELACION ENTRE SEXO Y HOMICIDIO


path_general='PYTHON_PROJECTS/PY-Pilatu-a-Zambrano-Isaac/proyecto_01/data'
filename_2015='/2015_data.csv'
filename_code_maps_2015='/code_maps_2015.json'
path_code_map=path_general+filename_code_maps_2015
columnas=['month_of_death','sex','detail_age','marital_status','day_of_week_of_death','358_cause_recode','current_data_year']

path=path_general+filename_2015
df_completo=pd.read_csv(
        path,
        usecols=columnas,
        keep_default_na=False
        )

try:
    with open(path_code_map,encoding="utf-8") as json_file:  
        code_maps_2015 = json.load(json_file)          
except:
    print("Error cargando code maps")
    
 

#Funcion para obtener las causas de muerte
df_completo['causa_muerte'] = df_completo['358_cause_recode'].apply(
    lambda x: code_maps_2015['%03d' % x])

#Referencia
#https://www.kaggle.com/sohier/mortality-data-format-v2-tutorial/


#Porcentaje casos de muerte por violación
violacion=df_completo['358_cause_recode']==439
df_casos_violacion=df_completo[violacion]
serie_count_violaciones=df_casos_violacion.sex.value_counts()
plt.pie(serie_count_violaciones,shadow=True,autopct='%1.1f%%',startangle=90)
plt.axis("equal")
plt.title("Muertes por violación")
plt.tight_layout()
plt.show()


#Top causas de muerte
serie_count_muertes=df_completo.causa_muerte.value_counts().head(5)
serie_count_muertes['Other']=df_completo.size-serie_count_muertes.sum()
patches,texts=plt.pie(serie_count_muertes,startangle=90,shadow=True)
plt.legend(patches,serie_count_muertes.index,loc="best")
plt.axis('equal')
plt.title("Top muertes")
plt.tight_layout()
plt.show()

serie_count_muertes_sin_otros=df_completo.causa_muerte.value_counts().head(5)
atches,texts=plt.pie(serie_count_muertes_sin_otros,startangle=90,shadow=True)
plt.legend(patches,serie_count_muertes_sin_otros.index,loc="best")
plt.axis('equal')
plt.title("Top muertes")
plt.tight_layout()
plt.show()




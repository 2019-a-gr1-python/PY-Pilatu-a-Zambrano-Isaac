import pandas as pd
import os
import json


path_general='PYTHON_PROJECTS/PY-Pilatu-a-Zambrano-Isaac/proyecto_01/data'
filename_2013='/2013_data.csv'
filename_2014='/2014_data.csv'
filename_2015='/2015_data.csv'

columnas=['month_of_death','sex','detail_age','marital_status','day_of_week','358_cause_recode','current_data_year']


#OBJETIVOS
#TOP CAUSAS DE MUERTE
#RELACION ENTRE SEXO Y SUICIDIO
#RELACION ENTRE ESTADO MARITAL Y SUICIDIO
#RELACION ENTRE SEXO, ESTADO MARITAL Y SUICIDIO
#RELACION ENTRE SEXO Y HOMICIDIO

#Funcion para obtener las causas de muerte
#data_2015['decoded_358_cause'] = data_2015['358_cause_recode'].apply(
#    lambda x: code_maps_2015['358_cause_recode'][x])

#Referencia
#https://www.kaggle.com/sohier/mortality-data-format-v2-tutorial/


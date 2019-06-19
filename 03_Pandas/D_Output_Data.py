#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 07:23:10 2019
@author: USRDEL
"""

import pandas as pd
import numpy as np
import os
import sqlite3

path_general='PYTHON_PROJECTS/PY-Pilatu-a-Zambrano-Isaac/03_Pandas/'
path_guardado=path_general+'data/csv/artwork_data.pickle'

df_completo_pickle = pd.read_pickle(path_guardado)

# Tres Archivos para exportar los datos
# Json
# SQL
# Excel

# Crear un df mas pequeño para que no se demore

df = df_completo_pickle.iloc[49980:50019,:].copy()

#############EXCEL#####################3

df.to_excel(path_general+'ejemplo_basico.xlsx')

#Quitar los indices

df.to_excel(path_general+'ejemplo_basico_sin_indices.xlsx', index=False)

#Trear columnas especificas 
columnas = ['artist','title','year']

df.to_excel(path_general+'columnas.xlsx', columns = columnas)


# Multiples hojas de trabajo (worksheet)

writer = pd.ExcelWriter(path_general+'multiples_worksheet.xlsx',
                        engine = 'xlsxwriter')

df.to_excel(writer, sheet_name = 'Preview')
df.to_excel(writer, sheet_name = 'Preview Dos', index = False)
df.to_excel(writer, sheet_name = 'Preview Tres', columns = columnas)

writer.save()


# Formateo Condicional

artistas_contados = df_completo_pickle['artist'].value_counts()

writer = pd.ExcelWriter(path_general+'colores.xlsx', engine = 'xlsxwriter')

artistas_contados.to_excel(writer, sheet_name = 'Artistas contados')

hoja_artistas = writer.sheets['Artistas contados']


#Cuantos artistas existen 
rango_celdas = 'B2:B{}'.format(len(artistas_contados.index)+1) #Para que se escogan todas las filas

formato = {
        'type': '2_color_scale',
        'min_value': '10',
        'min_type': 'percentile',
        'min_value': '99',
        'max_type': 'percentile'
        }

hoja_artistas.conditional_format(rango_celdas,formato)

writer.save()


######################### SQL ##################################

with sqlite3.connect(path_general+'bdd_python.db') as conexion:
    df.to_sql('Tabla', conexion)
    
## with mysql.connect('mysql://user:password@ip:puerto/bd') as conexion
##    df.to_sql('Tabla', conexion)

######################### JSON #################################

df.to_json(path_general+'artist.json')

df.to_json(path_general+'artist_ordientados_tabla.json', orient='table')




#EJERCICIO 
def ejercicio():
    writer = pd.ExcelWriter(path_general+'ejercicios.xlsx', engine = 'xlsxwriter')
    df['width']=df['width'].astype(float)
    df['height']=df['height'].astype(float)
    df['area']=df['width']*df['height']
    df['direccion']=np.random.randint(1,5,size=(len(df.index)))
    df['signal']=np.random.randint(1,6,size=(len(df.index)))
    df['negative']=np.random.randint(-5,6,size=(len(df.index)))
    df.to_excel(writer, sheet_name='Ejercicio_1')
    hoja_ejercicio_1=writer.sheets['Ejercicio_1']
    rango_celdas_1 = 'G2:G{}'.format(len(df.index)+1)                       
    formato_1 = {
            'type': '2_color_scale',
            'min_value': '10',
            'min_type': 'percentile',
            'min_value': '99',
            'max_type': 'percentile'
            }
    hoja_ejercicio_1.conditional_format(rango_celdas_1,formato_1)
    
    rango_celdas_2 = 'H2:H{}'.format(len(df.index)+1)
    formato_2 = {'type': '3_color_scale'}
    hoja_ejercicio_1.conditional_format(rango_celdas_2,formato_2)
    
    
    rango_celdas_3 = 'J2:J{}'.format(len(df.index)+1)
    formato_3 = {'type': 'data_bar',
                 'bar_color': '#DD4F5E'}
    hoja_ejercicio_1.conditional_format(rango_celdas_3,formato_3)
    
    rango_celdas_4 = 'K2:K{}'.format(len(df.index)+1)
    formato_4 = {'type': 'icon_set',
                 'icon_style': '4_arrows'}
    hoja_ejercicio_1.conditional_format(rango_celdas_4,formato_4)
    
    rango_celdas_5 = 'L2:L{}'.format(len(df.index)+1)
    formato_5 = {'type': 'icon_set',
                 'icon_style': '5_ratings'}
    hoja_ejercicio_1.conditional_format(rango_celdas_5,formato_5)
    
    rango_celdas_6 = 'M2:M{}'.format(len(df.index)+1)
    formato_6 = {'type': 'data_bar',
                 'bar_color': '#63C384',
                 'bar_negative_color': '#e01645'}
    hoja_ejercicio_1.conditional_format(rango_celdas_6,formato_6)
    
    writer.save()
    
ejercicio()
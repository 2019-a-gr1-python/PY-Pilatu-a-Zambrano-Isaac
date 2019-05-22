import numpy as np
import pandas as pd

lista_numeros=[1,2,3,4,]
tupla_numeros=(1,2,3,4,5)
numpy_numeros=np.array([1,2,3,4,5,6])
lista_serie=pd.Series(lista_numeros)
tupla_serie=pd.Series(tupla_numeros)
numpy_serie=pd.Series(numpy_numeros)

serie_objetos=pd.Series(
        [
        True,
        False,
        12,
        12.443,
        "String",
        None,
        (),
        [],
        {}
        ]
        )

lista_ciudades=["Quito","Ambato","Guayaquil","Portoviejo"]

serie_ciudades=pd.Series(lista_ciudades,index=["Q","A","G","P"])

type(serie_ciudades)

valores_ciudad={
        "Ibarra":9500,
        "Guayaquil":10000,
        "Cuenca":7000,
        "Quito":8000,
        "Loja":3000
        }
serie_valor_ciudad=pd.Series(valores_ciudad)
ciudades_menores_5000=serie_valor_ciudad < 5000
serie_ciudades_menos_5000=serie_valor_ciudad[ciudades_menores_5000]

serie_valor_ciudad*=1.1


print("Lima" in serie_valor_ciudad) #False
print("Loja" in serie_valor_ciudad)  #True

serie_valor_ciudad.any(3300)
serie_valor_ciudad = 3300

ciudades_uno=pd.Series({
        "Loja":4000
        })

ciudades_dos=pd.Series({
        "Montañita":300,
        "Guayaquil":10000,
        "Quito":2000
        })

print(ciudades_uno*ciudades_dos)

randomico=np.random.rand(3)
series_tres_rand=pd.Series(randomico)

ciudades_uno.index
test=pd.Series((ciudades_uno,ciudades_dos))

#Concatenar series
ciudades_combinadas=pd.concat([ciudades_uno,ciudades_dos])


#Agregar indice y valor a una serie
ciudades_combinadas.append(pd.Series({"Ambato":2000}))
#Maximo
pd.Series.max(ciudades_combinadas)
np.max(ciudades_combinadas)
#Minimo
pd.Series.min(ciudades_combinadas)
np.min(ciudades_combinadas)
#Average
pd.Series.mean(ciudades_combinadas)
np.average(ciudades_combinadas)

#Primeros 2 elementos
ciudades_uno.head(2)
#ultimos 2 elementos
ciudades_uno.tail(2)
#Ordenar elementos de forma ascendente
ciudades_dos.sort_values()
#Ordenar elementos de forma descendente
ciudades_dos.sort_values(ascending=False)

def impuesto(x):
    if (x<=1000):
        return x*1.05
    if (x<=10000):
        return x*1.1
    if(x>10000):
        return x*1.15
    
ciudades_dos
ciudades_dos.map(impuesto)



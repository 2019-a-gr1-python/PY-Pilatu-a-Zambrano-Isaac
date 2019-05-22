import numpy as np
import pandas as pd

arr_rand=np.random.randint(0,10,6).reshape(2,3)
df=pd.DataFrame(
        arr_rand,
        columns=['Estatura (cm)','Peso (Kg)','Edad'],
        index=['12','13']
        )

df_2=pd.DataFrame(
        arr_rand
        )

df_3=pd.DataFrame(
        arr_rand
        )

df_2.columns=['Estatura (cm)','Peso (Kg)','Edad']

df_3[0]

type(df_3[0])

df_2['Estatura (cm)']

df_2['Estatura (cm)'][0]


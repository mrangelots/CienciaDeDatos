""" Pipeline de Preprocesamiento """
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd

df = pd.DataFrame ({
    'precio': [100,200,300,400],
    'habitaciones': [1,2,1,3],
    'tipo': ['Casa', 'Apto', 'Casa', 'Apto']
})

# Definimos que columnas son cada una
col_nums = ['precio', 'habitaciones']
col_cate = ['tipo']

# Creamos nuestros transformador de columnas
procesador = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), col_nums),
        ('cat', OneHotEncoder(), col_cate)    
    ])

# Creamos nuestro pipeline completo
pipline_final = Pipeline(steps=[
    ('procesar', procesador)
])

# Lo aplicamos a todo
datos_listos = pipline_final.fit_transform(df)

print(f"Datos transformados por el Pipeline:\n{datos_listos}")
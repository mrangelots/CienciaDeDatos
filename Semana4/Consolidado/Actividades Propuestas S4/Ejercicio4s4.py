""" Manejo de Valores Faltantes """
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, np.nan],
    'C': [1, 2, 3, 4, 5]
})
# Calculamos porcentaje
porcentaje_faltante = (df.isnull().sum() / len(df)) * 100
# El inspector marca las filas que faltan
filasConNulos = df.isnull().any(axis=1)
soloFaltantes = df[filasConNulos]

# Si pone False es que hay un valor, si retorna un True significa que falta un valor 
print(f"Identificando valores faltantes:\n{df.isnull()}")
print(f"Contar los valores faltantes:\n{df.isnull().sum()}")
print(f"Porcentaje de valores faltantes:\n{porcentaje_faltante}")
print(f"Los filas con nulos son:\n{soloFaltantes}")

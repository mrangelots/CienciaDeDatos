""" Estrategias de Imputación """
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, np.nan],
    'C': [1, 2, 3, 4, 5]
})

# Eliminamos Filas con con datos nulos
dfFilasLimpias = df.dropna()

# Eliminamos Columnas con datos nulos
dfColumnasLimpias = df.dropna(axis=1)

# Imputando con la Media (Calculando el promedio de cada columna y rellenamos)
dfMedia = df.fillna(df.mean(numeric_only=True))

# Imputando con la Mediana. Ideal cuando tenemos valores extremos
dfMediana = df.fillna(df.median(numeric_only=True))

# Con Forward Fill el valor nulo toma el valor de la celda de arriba
dfFFill = df.ffill()

# Con Backward Fill el valor nulo toma el valor de la celda de abajo 
dfBFill = df.bfill()

print(f"Eliminando Filas con NULOS:\n{dfFilasLimpias}")
print(f"\nEliminando Columnas con NULOS:\n{dfColumnasLimpias}")
print(f"\nImputando con la Media:\n{dfMedia}")
print(f"\nImputando con la Mediana:\n{dfMediana}")
print(f"\nImputando con Foward:\n{dfFFill}")
print(f"\nImputando con Backward:\n{dfBFill}")

""" Imputación Avanzada """
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, np.nan],
    'C': [1, 2, 3, 4, 5]
})

# Estrategia de la Media
SImedia = SimpleImputer(strategy='mean')
# Medimos y rellenamos los datos
dCurMedia = SImedia.fit_transform(df)

# Estrategia de la Mediana
SImediana = SimpleImputer(strategy='median')
dCurMediana = SImediana.fit_transform(df)

# Estrategia Most_frequent (Moda)
SImost_frequent = SimpleImputer(strategy='most_frequent')
dCurMost_F = SImost_frequent.fit_transform(df)

# Estrategia Constant (Valor constante)
SIconstant = SimpleImputer(strategy='constant')
dCurConstant = SIconstant.fit_transform(df)

# Mostramos los datos
print(f"Datos imputados con MEDIA:\n{dCurMedia}")
print(f"\nDatos imputados con MEDIANA:\n{dCurMediana}")
print(f"\nDatos imputados con MOST_FREQUENT:\n{dCurMost_F}")
print(f"\nDatos imputados con CONSTANT:\n{dCurConstant}")

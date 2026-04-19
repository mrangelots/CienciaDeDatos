""" Transformaciones Numéricas """
import numpy as np
import pandas as pd
from scipy import stats

datos = [1, 2, 3, 4, 5, 10, 20, 30]

# Logaritmo natural (Comprime los datos)
datosLog = np.log(datos)

# Raíz cuadrada (Reduce la magnitud de los datos)
datosSqrt = np.sqrt(datos)

# Box-Cox (Busca matemáticamente un exponente para que los datos se parezcan lo más posible)
datosBoxCox, _ = stats.boxcox(datos)

# Discretización podemos vizualizar los datos de manera categoríca (rangos)
datosBinned = pd.cut(datos, bins= 3, labels=['Bajo', 'Medio', 'Alto'])

# Mostrando los datos
print(f"Datos Logaritmicos:\n{datosLog}")
print(f"\nDatos Raíz cuadrada:\n{datosSqrt}")
print(f"\nDatos Box-Cox:\n{datosBoxCox}")
print(f"\nDatos Binned:\n{datosBinned}")

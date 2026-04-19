""" Manejo de Outliers """
import numpy as np
from scipy import stats

datos = np.array([10, 12, 14, 15, 16, 18, 20, 22, 25, 100])

# Elimnar Outliers
datosFiltrados = datos[datos <= 32.375]

# Usando Capping
datosCapping = np.where(datos > 32.375, 32.375, datos)

# Usando Logarítmica
datosLog = np.log(datos)

# Usando Box-Cox
datosBoxCox, _ = stats.boxcox(datos)

# Mostramos resultados
print(f" Eliminación:\n{datosFiltrados}")
print(f" Capping:\n{datosCapping}")
print(f" Logarítmica:\n{datosLog}")
print(f" Box-Cox:\n{datosBoxCox}")
""" Método Z-Score """
from scipy import stats
import numpy as np 

datos = np.array([10, 12, 14, 15, 16, 18, 20, 22, 25, 100])

# Calculamos los scores
z_scores = stats.zscore(datos)

# Encontramos las posiciones donde el valor se Z > 3
indices_outliers = np.where(np.abs(z_scores) > 3)

# Mostramos los resultados
print(f"Z-Scores:\n{z_scores}")
print(f"\nÍndices de outliers:\n{indices_outliers}")

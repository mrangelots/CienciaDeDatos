""" Método IQR (Rango Intercuartil) """
import numpy as np

datos = [10, 12, 14, 15, 16, 18, 20, 22, 25, 100]

# Calculamos los cuartiles 1 y 3
q1 = np.percentile(datos, 25)
q3 = np.percentile(datos, 75)

# Calculamos el cuartil 2
iqr = q3 - q1 

# Calculamos los límites
limInf = q1 - (1.5 * iqr)
limSup = q3 + (1.5 * iqr)

# Indentificamos outliers
outliers = [x for x in datos if x < limInf or x > limSup]

# Mostramos los Resultados
print(f"Q1 = {q1}")
print(f"Q3 = {q3}")
print(f"IQR = {iqr}")
print(f"Lim Inferior = {limInf}")
print(f"Lim Superior = {limSup}")
print(f"Outliers: {outliers}")
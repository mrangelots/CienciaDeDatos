""" Estandarización (Z-Score) """
import math
# Lista de datos
x = [2, 4, 4, 4, 5, 5, 7, 9]
# Fórmulas para el ejercicio
m = sum(x) / len(x)
v = sum((i - m) ** 2 for i in x) / len(x)
de = v ** 0.5

# Estandarización 
z_score = []
for i in x:
    zs = (i - m) / de
    z_score.append(zs)

print(f"Los Valores Estanderizados:\n{z_score}")
print(f"La media: {m}")
print(f"Desviación Estandar: {de}")

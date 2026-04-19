""" Normalización Xmin-Xmax """
x = [10, 20, 30, 40, 50]
xn = []
# Sacamos los valores Max y Min
xmin = min(x)
xmax = max(x)
# Aplicando la fórmula a cada valor de X
for i in x:
    xnor = (i-xmin) / (xmax - xmin)
    xn.append(xnor)
# Imprimimos los resultados
print(f"Verificando los valores entre 0 y 1:\n{xn}")

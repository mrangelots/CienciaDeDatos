""" Ejercicio 5. """
import numpy as np

v1 = np.array([1,2,3]) 
v2 = np.array([4,5,6])

productoPunto = np.dot(v1,v2)
print(f"Producto punto: {productoPunto}")

productoCruz = np.cross(v1,v2)
print(f"Producto cruz: {productoCruz}")

magnitud_v1 = np.linalg.norm(v1)
magnitud_v2 = np.linalg.norm(v2)

print(f"Magnitud de v1: {magnitud_v1: .2f}")
print(f"Magnitud de v2: {magnitud_v2: .2f}")

# Normalizar el vector 1
v1_normalizado = v1 / magnitud_v1

# Verificación 
print(f"v1 normalizado: {v1_normalizado}")
print(f"Magnitud del vector normalizado: {np.linalg.norm(v1_normalizado)}")

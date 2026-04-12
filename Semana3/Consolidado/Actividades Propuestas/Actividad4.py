""" Ejercicio 4. """
import numpy as np

arr1 = np.array([1,28,17,12,3])
arr2 = np.array([1, 4, 2, 2, 1])
# Suma de arrays
suma = arr1 + arr2
print(f"Suma elemento a elemento {suma}")

# Multiplicar por un escalar
escalar = 3
producto = arr2 * escalar
print(f"\nMultiplicado por {escalar}: {producto}")

# Calcular Media, Mediana, Moda y DE
datos = np.array([10, 20, 30, 40, 50, 100])

media = np.mean(datos)
mediana = np.median(datos)
de = np.std(datos)

print(f"\nMedia: {media}")
print(f"Mediana: {mediana}")
print(f"DE: {de: .2f}")

# Encontrar valores unicos (Nos ayuda para limpiar los datos)
valores = np.array([1, 2, 2, 3, 4, 4, 4, 5])
valores_unicos = np.unique(valores)

print(f"Valores sin repetir: {valores_unicos}")

# Reshape  de 1D a 2D
arr1D = np.array([1,2,3,4,5,6])

# Lo convertimos a una matriz de 2 filas y 3 columnas
arr2D = arr1D.reshape(2,3)

print("Arrray 1D:")
print(arr1D)
print("\nNuevo Array (2D - 2x3)")
print(arr2D)


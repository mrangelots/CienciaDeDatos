""" Ejercicio 3. """
import math
# 1. Calcular el área de un círculo
def areaCirculo(r): 
    area = math.pi * (radio ** 2)
    return area
#Llamando a la función
radio = 5
resultadoArea = areaCirculo(radio)
print(f"El área del círculo con radio {radio} es:{resultadoArea: .2f}")

# 2. Convertir Celsius a Fahrenheit
def celciusFahrenheit(celcius):
    fahrenheit = (celcius * 1.8) + 32
    return fahrenheit
#Llamando a la función
grados_c = 25
print(f"{grados_c} equivalen a {celciusFahrenheit(grados_c)} °F")

# 3. Calcular el promedio de una lista
def promedioLista(lista):
    if not lista: 
        return 0
    suma = sum(lista)
    cantidad = len(lista)
    return suma / cantidad

#Llamando a la función
notas = [85, 90, 78, 92, 88]
promedioFinal = promedioLista(notas)
print(f"El promedio de la lista de los números es: {promedioFinal}")

# 4. Encontrar el valor máximo y mínimo
def encontrarExtremos (list):
    if not list:
        return 0
    maximo = max(list)
    minimo = min(list)
    return maximo, minimo

#Llamando a la función
datos = [10,5,80,3,15]
v_max, v_min = encontrarExtremos(datos)

print(f"En la lista {datos}")
print(f"El valor más alto es {v_max} y el mas bajo es {v_min}")

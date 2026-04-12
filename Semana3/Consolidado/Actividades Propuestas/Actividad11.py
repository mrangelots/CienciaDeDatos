""" Ejercicio 11. """
conjunto1 = [2, 4, 4, 4, 5, 5, 7, 9]
conjunto2 = [1, 3, 5, 7, 9]

def calcularMedia(lista):
    return sum(lista) / len(lista)

def calcularRango(lista):
    return max(lista) - min(lista)

def calcularVarianza(lista):
    media = calcularMedia(lista)
    n = len(lista)
    sumaCuadrados = 0
    for x in lista:
        sumaCuadrados += (x - media) ** 2
    return sumaCuadrados / n

def calcularDE(varianza):
    return varianza ** 0.5

def mostrarResultados(nombre, lista):
    #llamamos a nuestras funciones
    r = calcularRango(lista)
    v = calcularVarianza(lista)
    d = calcularDE(v)

    print(f"Rango: {r}")
    print(f"Varianza: {v}")
    print(f"Desviación Estandar: {d: .2f}")
    print("\n")

mostrarResultados("Lista 1.", conjunto1)
mostrarResultados("Lista 2.", conjunto2)
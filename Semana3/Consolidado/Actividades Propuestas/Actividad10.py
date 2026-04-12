""" Ejercicio 10. """
# Lista de números
listaA = [5, 3, 8, 3, 7]
listaB = [10, 20, 30, 40]
listaC = [1, 2, 2, 3, 3, 3, 4]

# Calcular Media
def calcularMedia(lista):
    sumaAcumulada = 0
    conteoElementos = 0
    for numero in lista:
        sumaAcumulada += numero
        conteoElementos += 1
    return sumaAcumulada / conteoElementos

# Calcular Mediana
def calcularMediana(lista):
    datos = sorted(lista)
    n = 0
    for _ in datos: n  += 1

    mitad = n // 2
    if n % 2 == 0:
        return (datos[mitad - 1] + datos[mitad]) / 2
    else:
        return datos[mitad]
    
# Calcular Moda
def calcularModa(lista):
    frecuencias = {}
    for numero in lista:
        if numero in frecuencias:
            frecuencias[numero] += 1
        else:
            frecuencias[numero] = 1
            
    max_visto = 0
    moda_resultante = None
    
    for numero, cantidad in frecuencias.items():
        if cantidad > max_visto:
            max_visto = cantidad
            moda_resultante = numero
            
    # Validación: si el máximo de repeticiones es 1, no hay moda real
    if max_visto == 1:
        return "N/A"
    return moda_resultante

print(" - - - RESULTADOS - - - \n")
print("--- RESULTADOS: MEDIA ---")
print(f"Lista A: {calcularMedia(listaA):.2f}")
print(f"Lista B: {calcularMedia(listaB):.2f}")
print(f"Lista C: {calcularMedia(listaC):.2f}\n")
print("--- RESULTADOS: MEDIANA ---")
print(f"Lista A: {calcularMediana(listaA):.2f}")
print(f"Lista B: {calcularMediana(listaB):.2f}")
print(f"Lista C: {calcularMediana(listaC):.2f}\n")
print("--- RESULTADOS: MODA ---")
print(f"Lista A: {calcularModa(listaA)}")
print(f"Lista B: {calcularModa(listaB)}")
print(f"Lista C: {calcularModa(listaC)}\n")


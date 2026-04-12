""" Ejercicio 2. """
# Positivo, Negativo o cero 
n = -67
if n > 0:
    print("Es positivo\n")
elif n < 0:
    print("Es negativo\n")
else:
    print("Es cero\n")

# Menú interactivo
print(" --- MENÚ --- ")
print(" 1. Saludar ")
print(" 2. Despedirse ")
print(" 3. Salir ")

# Simulamos que la opcion que se escoge es 1. 
opcion = 1

if opcion == 1:
    print("Hola un gusto verte :D")
elif opcion == 2:
    print("Adios, que tengas bonito día")
elif opcion == 3:
    print("Saliendo del programa")
else:
    print("OPción no valida")

# Loop for para iterar en una lista
frutas = ["Manzana","Naranja","Uva","Platano","Cereza","Fresa","Jicama"]

print("\n - - - Lista de futas - - - ")
for fruta in frutas:
    print(f"- {fruta}")

# Ciclo while para factorial
m = 5
factorial = 1
contador = m

while contador > 1:
    factorial *= contador
    contador -= 1

print(f"\nEl factorial es: {factorial}")

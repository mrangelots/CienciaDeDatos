""" Ejercicio 1. """
# Variables de diferentes tipos
edad = 19                                   #int
calificacion = 8.22                         #float
nombre = "Mateo"                            #str
esEstudiante = True                         #bool
materias = {"Programación", "Inglés II"}    #list
usuario = {                                 #dict
    "id": "AL07179280",
    "rol": "Profesional",
    "carrera": "IDS",
    "semestre": 2
}

# Convertir tipos
edad_texto = "19" 
edad_convertida = int(edad_texto)
calRedondeada = int(calificacion)
edadRedonda = float(edad)

# Uso de f-string
print(f"El usuario de nombre: {nombre} tiene {edad_convertida}")
print(f"Calificación redondeada: {calRedondeada}")




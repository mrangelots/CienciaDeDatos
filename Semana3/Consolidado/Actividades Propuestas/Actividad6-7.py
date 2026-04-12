""" Ejercicio 6 y  7. """
import pandas as pd
import numpy as np
data = {
    "nombre": ["Ana", "Luis", "María", "Carlos", "Sofia"],
    "edad": [20, 22, 19, 21, 23],
    "carrera": ["Ing", "Ing", "Lic", "Ing", "Lic"],
    "promedio": [8.5, 9.0, 7.8, 8.2, 9.5]
}

df = pd.DataFrame(data)

# 1. Seleccionar columna nombre
nombres = df["nombre"]
print("Columna de nombres: ")
print(nombres)

# 2. Filtrar alumnos con promedio > 8.5
excelentes = df[df["promedio"] > 8.5]
print("\nAlumnos con promedio mayor a 8.5")
print(excelentes)

# 3. Ordenar por edad
df_ordenado = df.sort_values(by="edad")
print("\nDatos ordenados por edades:")
print(df_ordenado)

# 4. Aprobados 
df["aprobados"] = df["promedio"] >= 7
print("\nAlumnos que aprobaron:")
print(df)

# 5. Group by carrera y promediar
promedioPorCarrera = df.groupby("carrera").mean(numeric_only=True)
print("\nPromedio general por carrera:")
print(promedioPorCarrera)

print("\nSegunda parte")

# Agregamos un valor nulo
df.loc[0,"edad"] = np.nan

print("Lista con valor nulo:")
print(df.head(2))

df["edad"] = df["edad"].fillna(df["edad"].mean())

print("\nDespués de llenar NaN:")
print(df.head(2))

# Creamos una fila duplicada para probar
df = pd.concat([df, df.iloc[[0]]], ignore_index=True)

# Eliminamos duplicados
df = df.drop_duplicates()
print("\nDuplicados eliminados")

# Función para categorizar el rendimiento
def categorizar(promedio):
    if promedio >= 9.0:
        return "Excelente"
    elif promedio >=8.0:
        return "Bueno"
    else:
        return "Regular"
    
# Aplicamos la función para crear una columna nueva

df["categoria"] = df["promedio"].apply(categorizar)
print("\nDataFrame con categorías:")
print(df[["nombre", "promedio", "categoria"]])

# Usar Loc e iLoc para slicing
dato_loc = df.loc[1, ["nombre", "carrera"]]
recorte_iloc = df.iloc[0:3, 0:2]

print("\nUso de loc (Etiquetas):")
print(dato_loc)
print("\nUso de iloc (Posiciones):")
print(recorte_iloc)

# Cocatenar un segundo DataFrame
data2 = {
    "nombre": ["Zoe", "Diego"],
    "edad": [22, 21],
    "carrera": ["Ing", "Lic"],
    "promedio": [9.1, 8.4]
}

df2 = pd.DataFrame(data2)

# Concatemos Data y Data2
df_total = pd.concat([df,df2], ignore_index=True)

print("\nData Frame concatenado:")
print(df_total)

""" Actividad 3.1 Refuerzo de Python """

import pandas as pd

# Creamos una lista de diccionarios que representan nuestros datos
datosSucursales = [
    {"sucursal": "Norte", "ventas": 25000, "gastos": 18000},
    {"sucursal": "Sur", "ventas": 32000, "gastos": 35000},
    {"sucursal": "Este", "ventas": 15000, "gastos": 12000},
    {"sucursal": "Oeste", "ventas": 40000, "gastos": 22000}
]

# Manejo de errores
try:
    df = pd.DataFrame(datosSucursales)
    print("Data Frame creado con éxito.")
except Exception as e:
    print(f"Error al procesar los datos {e}")

# Funcion Lambda para calcular el margen de beneficio (ventas - gastos)
# Aplicamos la funcion a cada fila del dataframe
df['beneficio'] = df.apply(lambda row: row['ventas'] - row['gastos'], axis=1)

# List Comprehensions nos ayudara a crear una lista que nos ayude a ver las pérdidas
sucursalesEnAlerta = [row['sucursal'] for _, row in df.iterrows() if row['beneficio'] < 0]

print("\n- - - Análisis de sucursales - - -")
print(df)
print(f"Sucursales que requieren una revisión: {sucursalesEnAlerta}")
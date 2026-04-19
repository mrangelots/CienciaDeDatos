""" Comparación de Técnicas """
# Preparamos la cocina (Importamos librerias) y nuestros datos
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

datos = np.array([100, 200, 300, 400, 500]).reshape(-1,1)

# Elegir el tipo de sandwich (Instaciamos los objetos)
s_scaler = MinMaxScaler()
# Medimos el jamon (llamamos a nuestra instancia)
datosNor = s_scaler.fit_transform(datos)

# Creamos el segundo sandwich 
s_standar = StandardScaler()
datosSta = s_standar.fit_transform(datos)

print("\n--- COMPARACIÓN ---")
print(f"Originales: {datos.flatten()}")
print(f"Min_Max {datosNor.flatten()}")
print(f"Standar: {datosSta.flatten()}")

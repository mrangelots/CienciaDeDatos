""" Ejercicio 8. """
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
y = np.sin(x)
# Gráfico de linea basico 
plt.plot(x,y)
plt.show()

# Gráfico de dispersión 
x_scatter = np.linspace(0,10,30)
y_scatter = np.sin(x_scatter)

plt.scatter(x_scatter, y_scatter, color="red")
plt.show()

# Histograma
datos_aleatorios = np.random.rand(1000)
plt.hist(datos_aleatorios, bins=30, color="skyblue", edgecolor="black" )
plt.show()

categorias = ['A', 'B', 'C', 'D']
valores = [23, 45, 12, 35]

plt.bar(categorias, valores, color='orange')
plt.show()

plt.plot(x, y, label='Seno(x)', color='purple', linestyle='--', linewidth=2)

# Personalización completa
plt.title("Gráfico de Ondas")        # <- Título principal
plt.xlabel("Eje X (Tiempo)")         # <- Etiqueta eje X
plt.ylabel("Eje Y (Amplitud)")       # <- Etiqueta eje Y
plt.legend()                         # <- Mostrar la leyenda (label)
plt.grid(True)                       # <- Agregar cuadrícula de fondo

plt.show()
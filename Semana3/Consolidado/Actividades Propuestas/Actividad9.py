""" Ejercicio 9. """
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Cargar el dataset
df = sns.load_dataset('iris')

# Mostramos información básica 
print("--- Primeras Filas ---")
print(df.head())
print("\n--- Estructura de los Datos ---")
df.info()

print("\n--- Resumen Estadístico ---")
print(df.describe())

# Creamos nuestro histograma 
sns.histplot(data=df, x='sepal_length', kde=True, color='green')
plt.title("Distribución del Largo del Sépalo")
plt.show()

# Calculamos la correlación de la filas numericas
corr = df.drop(columns='species').corr()

# Creamos un mapa de calor (Heatmap)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Matriz de Correlación")
plt.show()

sns.boxplot(data=df, x='species', y='petal_length', palette='Set2')
plt.title("Largo del Pétalo por Especie")
plt.show()

# Vizualizar de una forma más visual
sns.stripplot(data=df, x='species', y='sepal_width', color='black', alpha=0.3)
sns.boxplot(data=df, x='species', y='sepal_width')
plt.title("Identificación visual de Outliers en Ancho del Sépalo")
plt.show()
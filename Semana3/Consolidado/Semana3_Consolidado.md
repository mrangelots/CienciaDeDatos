# Semana 3

## 1. Ejercicios Complementarios

### 1. Variables y Tipos de Datos
Ejercicio: [Actividad1.py](<Actividades Propuestas/Actividad1.py>)

### 2. Control de Flujo
Ejercicio: [Actividad2.py](<Actividades Propuestas/Actividad2.py>)

### 3. Funciones
Ejercicio: [Actividad3.py](<Actividades Propuestas/Actividad3.py>)

### 4. Operaciones con Arrays
Ejercicio: [Actividad4.py](<Actividades Propuestas/Actividad4.py>)

### 5. Álgebra con NumPy
Ejercicio: [Actividad5.py](<Actividades Propuestas/Actividad5.py>)

### 6. DataFrames Básico y 7. Manipulación de Datos
Ejercicio: [Actividad6-7.py](<Actividades Propuestas/Actividad6-7.py>)

### 8. Matplotlib
Ejercicio: [Actividad8.py](<Actividades Propuestas/Actividad8.py>)

### 9. Análisis Exploratorio
Ejercicio: [Actividad9.py](<Actividades Propuestas/Actividad9.py>)

### 10. Medidas de Tendencia Central
Ejercicio: [Actividad10.py](<Actividades Propuestas/Actividad10.py>)

### 11. Dispersion
Ejercicio: [Actividad11.py](<Actividades Propuestas/Actividad11.py>)

### 12. El Proceso de Data Science
#### ¿Qué es el ciclo CRISP-DM?
`CRIPS-DM` significa Cross-Industry Standard Process for Data Mining. Es el modelo más utilizado en el mundo para guiar proyectos de minería de datos y ciencia de datos.

Su característica principal es que es un proceso cíclico: no termina cuando entregas el resultado, sino que los hallazgos suelen generar nuevas preguntas a lo que lleva a repetir el ciclo nuevamente 

#### ¿Cuáles son las fases del proceso de ciencia de datos? 

1. Compresión del Negocio
    * ¿Qué queremos predecir o descubrir?
2. Compresión de los datos
    * Recolectar los datos iniciales y explorarlos para ver que calidad tienen que nos quieren decir a simple vista
3. Preparación de los Datos
    * Se limpian los datos
    * Se manejan valores nulos
    * Se seleccionan la variables más importantes
4. Modelado
    * Se seleccionan y aplican las técnicas matemáticas o algoritmos 
5. Evaluación 
    * Revisar si relamente el modelo resuelve la problematica del negocio definido en el paso 1
6. Despliegue
    * Poner el modelado en funcionamiento 

#### ¿Qué es el MVP (Minimum Viable Product) en ciencia de datos?

El Producto Mínimo Viable es la versión más sencilla de de un modelo o análisis que ya entrega el valor al usuario 

* En Ciencia de datos: En lugar de construir un sistema de Inteligencia Artificial súper complejo que tarde un año, el MVP sería un modelo simple

* Propósito: Validar rápido si los datos sirven para resolver el problema antes de gastar mucho tiempo y dinero en algo más complejo.

### 13. Caso de Estudio: Análisis de Supervivencia del Titanic

#### ¿Qué preguntas buscaban responder?

El objetivo principal era entender qué factores influyeron en que una persona sobreviviera o no al naufragio. Las preguntas clave eran:

* ¿Influyó la clase social (1ª, 2ª o 3ª clase) en la probabilidad de sobrevivir?

* ¿Se cumplió realmente la política de "mujeres y niños primero"?

* ¿Tener familiares a bordo ayudó o dificultó la salvación?

#### ¿Qué técnicas usaron?

* Al ser un análisis exploratorio, se utilizaron técnicas estadísticas y visuales básicas:

* Histogramas y Gráficos de Barras: Para comparar cuántos hombres vs. mujeres sobrevivieron.

* Cálculo de Proporciones: Comparar el porcentaje de sobrevivientes por clase (ej. % en 1ª clase vs % en 3ª clase).

* Detección de valores nulos: Identificar que faltaban muchos datos de la variable "Edad" y "Cabina".

* Matriz de Correlación: Para ver si existía una relación matemática entre el precio del boleto y la supervivencia.

#### ¿Qué insights encontraron?

Los `insights` son los hallazgos o descubrimientos clave del análisis. Estos fueron los siguientes:

* Desigualdad de Clase: Los pasajeros de primera clase tuvieron una tasa de supervivencia significativamente mayor que los de tercera.

* Prioridad de Género: El género fue el predictor más fuerte. Las mujeres tuvieron una probabilidad de sobrevivir mucho más alta que los hombres, sin importar su edad.

* Factor Edad: Los niños (menores de 15 años) tuvieron prioridad, pero esto fue mucho más evidente en las clases altas que en la tercera clase.

## 2. Actividades Prácticas

### Actividad 3.1
Entregable: [Actividad3-1.md](../Actividades/Actividad3.1/Actividad3-1.md)

### Actividad 3.2
Entregable: [Actividad3-2.ipynb](../Actividades/Actividad3.2/Actividad3-2.ipynb)

### Actividad 3.3
Entregable: [Actividad3-3.ipynb](../Actividades/Actividad3.3/Actividad3-3.ipynb)

### Actividad 3.4
Entregable: [Actividad3-4.ipynb](../Actividades/Actividad3.4/Actividad3-4.ipynb)

## 3. Resumen de Aprendizaje 

* Aprendimos a saber hacer un análisis de nuestros datos
* Entender nuestro Data para saber que tipos de datos tenemos
* Tomar la decisión de saber si modificamos o cancelamos ciertos datos
* Leer resultados

## 4. Dudas o Preguntas
* Practicar ejercicios con librerias para familiarizar
* ¿Podemos ver mas sobre entornos virtuales?

## 5. Referencias
- https://www.datascience-pm.com/crisp-dm-2/
- Dataset Titanic:
    - https://www.kaggle.com/c/titanic
- Documentación de las librerías (Pandas y Seaborn):
    - https://pandas.pydata.org/docs/
    - https://seaborn.pydata.org/

## 6. Actividad semanal
Entregable: [Analisis_EDA.ipynb](../Proyecto/Avance/Analisis_EDA.ipynb)

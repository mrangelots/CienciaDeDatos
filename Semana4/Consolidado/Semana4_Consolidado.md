# Semana 4

## 1. Ejercicios Complementarios

### 1. Normalización Min-Max
Ejercicio: [Ejercicio1s4.py](<Actividades Propuestas S4/Ejercicio1s4.py>)

### 2. Estandarización (Z-Score)
Ejercicio: [Ejercicio2s4.py](<Actividades Propuestas S4/Ejercicio2s4.py>)

### 3. Comparación de Técnicas
Ejercicio: [Ejercicio3s4.py](<Actividades Propuestas S4/Ejercicio3s4.py>)

### 4. Identificación de Valores Faltantes
Ejercicio: [Ejercicio4s4.py](<Actividades Propuestas S4/Ejercicio4s4.py>)

### 5. Estrategias de Imputación
Ejercicio: [Ejercicio5s4.py](<Actividades Propuestas S4/Ejercicio5s4.py>)

### 6. Imputación Avanzada
Ejercicio: [Ejercicio6s4.py](<Actividades Propuestas S4/Ejercicio6s4.py>)

### 7. Método IQR (Rango Intercuartil)
Ejercicio: [Ejercicio7s4.py](<Actividades Propuestas S4/Ejercicio7s4.py>)

### 8. Método Z-Score
Ejercicio: [Ejercicio8s4.py](<Actividades Propuestas S4/Ejercicio8s4.py>)

### 9. Manejo de Outliers
Ejercicio: [Ejercicio9s4.py](<Actividades Propuestas S4/Ejercicio9s4.py>)

### 10. Codificación de Variables Categóricas
Ejercicio: [Ejercicio10s4.py](<Actividades Propuestas S4/Ejercicio10s4.py>)

### 11. Transformaciones Numéricas
Ejercicio: [Ejercicio11s4.py](<Actividades Propuestas S4/Ejercicio11s4.py>)

### 12. Feature Engineering
Ejercicio: [Ejercicio12s4.py](<Actividades Propuestas S4/Ejercicio12s4.py>) 

### 13. Comparar Escaladores
Ejercicio: [Ejercicio13s4.py](<Actividades Propuestas S4/Ejercicio13s4.py>)

### 14. Pipeline de Preprocesamiento
Ejercicio: [Ejercicio14s4.py](<Actividades Propuestas S4/Ejercicio14s4.py>)

### 15. Mejores Prácticas

```md
#### ¿Por qué es importante la preparación de datos?

En el mundo de la IA existe una regla de oro: "Garbage In, Garbage Out" (Si entra basura, sale basura). Por muy avanzado que sea el algoritmo, si los datos están sucios, los resultados serán mediocres o falsos.

* *Calidad sobre Cantidad:*
    * Los modelos de Machine Learning aprenden patrones. Si los datos tienen ruido, el modelo aprendera el ruido y se olvidara del patrón real

* *Compatibilidad Matemática:*
    * La mayoría de los algoritmos no pueden procesar texto directamente ni manejar celdas vacías. La preparación traduce la realidad al lenguaje de las matrices.

* *Sesgo y Equidad:*
    * Preparar los datos permite identificar y corregir sesgos que podrían llevar a decisiones injustas o discriminatorias

#### ¿Qué es Data Leakage y cómo evitarlo?

El Data Leakage (Fuga de datos) ocurre cuando información del "futuro" o del conjunto de prueba se filtra en el modelo durante el entrenamiento

* *¿Comó sucede?*
    * Cuando usamos datos que conoceríamos despues de que ocurra el evento que queremos predecir
    * Mezclando información, es cuando los datos que vamos a evaluar los combinamos con los datos que el modelo estudia

* *¿Comó prevenir?*
    * Asilamiento total
    * Simulando la realidad
    * Procesar por separado

#### Diferencia entre datos de entrenamiento y prueba

| Característica | Datos de Entrenamiento                         | Datos de prueba                              |
|----------------|------------------------------------------------|----------------------------------------------|
| Propósito      | Enseñar al modelolos patrones y las relaciones | Evaluar el desempeño real del modelo.        |
| Volumen        | Típicamente el 70% - 80% de los datos.         | Típicamente el 20% - 30% de los datos.       |
| Uso            | Se usa para ajustar los pesos del algoritmo.   | Solo se usa para "calificar" al modelo final.|
```

### 16. Técnicas Avanzadas

```md
#### ¿Qué es SMOTE para datos desbalanceados?

SMOTE (`S`ynthetic `M`inority `O`ver-sampling `T`echnique) es una técnica de aumento de datos inteligente

* *¿Para qué sirve?*
Equilibrar las oportunidades de aprendizaje del modelo.
    * Sirve para evitar que el modelo ignore por completo a los grupos minoritarios.

#### ¿Qué es la imputación por K-Nearest Neighbors?
* *¿Para qué sirve?*
Rellenar vacíos basándose en el contexto y la similitud.
    * Sirve para rescatar filas que tienen datos faltantes sin inventar valores al azar o usar promedios generales que no tienen sentido.

#### ¿Qué es Target Encoding?
* *¿Para qué sirve?*
Convertir categorías complejas en información directamente relacionada con el éxito de la predicción.
    * Sirve para manejar columnas que tienen demasiadas categorías (como códigos postales, nombres de marcas o tipos de modelos) donde el One-Hot Encoding crearía miles de columnas innecesarias.
```
## 2. Actividades Prácticas

### Actividad 4.1

Entregable: [Actividad4-1.ipynb](../Actividades/Actividad4.1/Actividad4-1.ipynb)

### Actividad 4.2

Entregable: [Actividad4-2.ipynb](../Actividades/Actividad4.2/Actividad4-2.ipynb)

### Actividad 4.3

Entregable: [Actividad4-3.ipynb](../Actividades/Actividad4.3/Actividad4-3.ipynb)

### Actividad 4.4

Entregable: [Actividad4-4.ipynb](../Actividades/Actividad4.4/Actividad4-4.ipynb)

## 3. Resumen de Aprendizaje

* Limpieza de datos y como cada una se puede adaparte de distinta manera y como los datos los podemos expresar de una manera distinta, sin perder nada
* El saber como podemos manejar los valores nulos
* Como es que la Media, Mediana y Moda juegan un papel crucial en nuestros datos y como nos podemos apoyar de estas herramientas

## 4. Dudas o Preguntas

* ¿Como podemos mejorar el relacionar la limpieza con nuestra manera de interpretar los datos?

## 5. Referencias

* https://scikit-learn.org/stable/common_pitfalls.html
* https://www.oreilly.com/library/view/feature-engineering-for/9781491953235/
* https://www.jair.org/index.php/jair/article/view/10302

## 6. Actividad semanal

Entregable: [Analisis.ipynb](../Actividades/Actividad3/Analisis.ipynb)

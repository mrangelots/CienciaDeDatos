# Reporte Actividad 1
---
## Perfiles de ciencia de datos y su importancia en DeportivaMX
Dado que la problemática principal de DeportivaMX es el crecimiento acelerado en sus ventas y la falta de infraestructura adecuada para gestionar sus datos, resulta fundamental contar con un equipo especializado que permita estructurar, analizar y aprovechar la información de manera eficiente. Cada uno de los siguientes perfiles cumple una función clave para resolver esta situación y optimizar la toma de decisiones a corto y mediano plazo.

En primer lugar, el `Data Engineer` es responsable de construir y mantener la infraestructura de datos. Su función principal es garantizar que la información proveniente de diversas fuentes, como ventas, clientes y productos, esté limpia, organizada y disponible. Esto permite que los datos puedan ser analizados de forma eficiente, asegurando su calidad, seguridad y accesibilidad, lo cual es esencial para una empresa en crecimiento.

Por otro lado, el `Data Analyst` se encarga de interpretar los datos históricos y transformarlos en información comprensible para el negocio. Este perfil permite identificar patrones de comportamiento, tendencias de ventas y áreas de mejora, como la optimización del inventario o estrategias comerciales. Gracias a su trabajo, la empresa puede tomar decisiones informadas que impacten positivamente en su rendimiento a corto y mediano plazo.

El `Data Scientist` utiliza métodos científicos y estadísticos para analizar grandes volúmenes de datos y generar modelos predictivos. Su objetivo es anticipar escenarios futuros, como proyecciones de ventas, comportamiento del cliente o posibles oportunidades de crecimiento. Esto permite a DeportivaMX tomar decisiones estratégicas basadas en datos y no únicamente en intuición.

Asimismo, el `Machine Learning Engineer` es el encargado de llevar los modelos desarrollados por el Data Scientist a entornos de producción. Mediante el uso de prácticas como MLOps, automatiza el entrenamiento y actualización de los modelos, evitando su degradación con el tiempo. Esto permite escalar soluciones basadas en inteligencia artificial y manejar grandes volúmenes de datos de manera eficiente.

Finalmente, el `Data Architect` define la estrategia global de los datos dentro de la organización. Este perfil se encarga de diseñar arquitecturas de datos escalables y seguras, así como de establecer políticas de gobernanza y cumplimiento normativo, especialmente en temas de privacidad. Además, selecciona las tecnologías adecuadas para garantizar un manejo eficiente de la información y facilitar su análisis.

> En conjunto, estos perfiles permiten a DeportivaMX no solo gestionar su crecimiento, sino también transformar sus datos en una ventaja competitiva, mejorando la experiencia del cliente y optimizando sus procesos internos.

## Las 5 V del Big Data en DeportivaMX
### *1. Volumen*

El volumen se refiere a la gran cantidad de datos que genera la empresa. En el caso de DeportivaMX, el crecimiento acelerado ha provocado un incremento significativo en la información generada, como registros de ventas, datos de clientes y características de productos.
Este gran volumen de datos requiere herramientas y tecnologías capaces de almacenarlos y procesarlos de manera eficiente.

### *2. Velocidad*

La velocidad hace referencia a la rapidez con la que los datos son generados y deben ser procesados. En DeportivaMX, las transacciones de ventas ocurren constantemente, por lo que es importante procesar esta información casi en tiempo real para tomar decisiones rápidas, como ajustar inventarios o lanzar promociones.

### *3. Variedad*

La variedad se relaciona con los diferentes tipos de datos que maneja la empresa. DeportivaMX trabaja con datos estructurados (como bases de datos de ventas), semiestructurados (como archivos JSON) y no estructurados (como opiniones de clientes o interacciones en redes sociales).
Esta diversidad hace necesario contar con tecnologías flexibles que permitan integrar toda esta información.

### *4. Veracidad*

La veracidad se refiere a la calidad y confiabilidad de los datos. En una empresa en crecimiento como DeportivaMX, es fundamental asegurar que la información sea precisa y esté limpia, evitando errores que puedan afectar la toma de decisiones.
Por ello, procesos como la limpieza y validación de datos son esenciales.

### *5. Valor*

El valor es la capacidad de transformar los datos en información útil para el negocio. En este caso, DeportivaMX puede utilizar sus datos para identificar patrones de compra, mejorar la experiencia del cliente, optimizar inventarios y aumentar sus ventas.
El verdadero objetivo del Big Data es generar ventajas competitivas a partir de la información.
 
> En conjunto, las 5 V del Big Data permiten a DeportivaMX comprender mejor la complejidad de sus datos y la importancia de gestionarlos adecuadamente, facilitando la toma de decisiones estratégicas y el crecimiento sostenible de la empresa.

---

## Arquitectura de datos para DeportivaMX
Debido al crecimiento acelerado de DeportivaMX y al incremento en la cantidad de datos generados, es necesario implementar una arquitectura de datos moderna que permita almacenar, procesar y analizar la información de manera eficiente, escalable y segura. En este caso, se propone el uso de una arquitectura basada en un Data Lake.

El Data Lake es una solución que permite almacenar grandes volúmenes de datos en su formato original, sin necesidad de estructurarlos previamente. Esto es ideal para DeportivaMX, ya que maneja distintos tipos de información como ventas, datos de clientes, productos y posibles interacciones digitales.

Ventajas: 
* Permite almacenar datos estructurados, semiestructurados y no estructurados
* Es altamente escalable, ideal para el crecimiento de la empresa
* Facilita el análisis avanzado y el uso de modelos de Machine Learning
* Reduce costos al no requerir transformación inmediata de los datos

### Flujo de datos propuestos
* Recolección de datos
    - Se obtienen datos de ventas, clientes y productos.
* Almacenamiento en Data Lake
    - Los datos se guardan en su formato original.
* Procesamiento y limpieza
    - El Data Engineer prepara los datos para su análisis.
* Análisis y modelado
    - El Data Analyst y Data Scientist generan insights y modelos predictivos.
* Visualización y toma de decisiones
    - Se utilizan dashboards para apoyar decisiones estratégicas.

---

## Base de datos NoSQL: MongoDB
Para complementar la arquitectura, se propone el uso de una base de datos NoSQL como MongoDB, ya que se adapta perfectamente a las necesidades de flexibilidad de DeportivaMX.

¿Por qué MongoDB?

MongoDB es una base de datos orientada a documentos que almacena la información en formato JSON, lo que la hace ideal para manejar datos variados y en constante cambio.

Ventajas para el caso:
* Permite manejar datos flexibles y no estructurados
* Es fácil de escalar conforme crece la empresa
* Se integra bien con aplicaciones modernas
* Ideal para almacenar información de clientes, productos y ventas

> En DeportivaMX, donde existe una gran variedad de datos y cambios constantes en la información, MongoDB permite almacenar registros sin una estructura rígida. Esto facilita la adaptación a nuevas necesidades del negocio, como agregar nuevos atributos a productos o analizar el comportamiento del cliente sin modificar toda la base de datos.

## Colecciones en formato JSON
### Clientes
```json
{
  "_id": "C001",
  "nombre": "Juan Pérez",
  "correo": "juanperez@email.com",
  "telefono": "4421234567",
  "direccion": {
    "ciudad": "Querétaro",
    "estado": "Querétaro"
  },
  "historial_compras": ["V001", "V002"]
}
```
### Productos
```json
{
  "_id": "P001",
  "nombre": "Tenis deportivos",
  "marca": "Nike",
  "precio": 1499.99,
  "stock": 50,
  "categoria": "Calzado",
  "tallas_disponibles": [25, 26, 27, 28]
}
```
### Ventas
```json
{
  "_id": "V001",
  "cliente_id": "C001",
  "fecha": "2026-03-20",
  "productos": [
    {
      "producto_id": "P001",
      "cantidad": 1,
      "precio_unitario": 1499.99
    }
  ],
  "total": 1499.99,
  "metodo_pago": "Tarjeta"
}
```
> Para la implementación de la base de datos NoSQL se utilizaría MongoDB Compass como interfaz gráfica, donde se crearían colecciones como clientes, productos y ventas. En cada colección se insertarían documentos en formato JSON, permitiendo visualizar y gestionar los datos de manera flexible.
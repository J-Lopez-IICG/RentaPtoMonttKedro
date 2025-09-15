# Análisis de Mercado de Arriendos en Puerto Montt

---

## Resumen del Proyecto

Este proyecto se desarrolló para resolver el desafío de la **falta de datos estructurados** en el mercado de arriendos de Puerto Montt. El objetivo principal fue construir una solución de análisis de principio a fin, desde la **recolección de datos de la web** hasta la creación de un **dashboard interactivo** que ofrece una visión clara del mercado inmobiliario.

---

## Desafíos y Soluciones

El núcleo de este proyecto fue el desarrollo de un pipeline de datos robusto que demuestra las siguientes habilidades:

* **Web Scraping Dinámico:** Se utilizó **Python con Selenium** para automatizar la extracción de datos de un sitio web de bienes raíces. Esto fue crucial para manejar desafíos como la paginación y la estructura cambiante del sitio, obteniendo información sobre más de 600 arriendos.

* **Limpieza y Transformación de Datos:** Los datos extraídos fueron procesados en **Power Query** para garantizar su calidad. Se realizaron transformaciones clave como la estandarización de variables y la conversión de precios para un análisis consistente.

* **Análisis con Power BI:** Se desarrollaron métricas clave **(KPIs)** y visualizaciones interactivas para explorar el conjunto de datos y presentar los hallazgos de forma clara, permitiendo la toma de decisiones informadas.

---

## Dashboard Interactivo y Hallazgos Clave

El análisis culminó en un dashboard en Power BI que sirve como una herramienta para explorar las dinámicas del mercado de arriendos.

**Explora el dashboard aquí:** [Análisis del Mercado de Arriendos en Power BI]( https://app.powerbi.com/view?r=eyJrIjoiZmEzMTI5OTctNDA2Zi00MTMyLWJiZjEtY2E3ZjI2MWEzZTI4IiwidCI6ImRmNGI2MzcyLWEwM2EtNDZmMC05YmY1LTdmOGQzNzhhMzMzNCIsImMiOjR9 )

**Hallazgos Principales:**

* **Precio por m²:** El precio promedio por metro cuadrado de los arriendos es de 2.445 mil pesos, lo que sirve como un punto de referencia clave para evaluar la eficiencia de las propiedades.
* **Correlación de Precios:** Se identificó una fuerte correlación positiva entre el tamaño de la propiedad (m²) y el precio de arriendo.
* **Comparativa de Propiedades:** A pesar de que las casas tienen un precio de arriendo promedio más alto, los **departamentos son significativamente más caros por metro cuadrado**, un hallazgo crucial para quienes buscan maximizar el espacio por su inversión.

---

## Tecnologías y Código

* **Herramientas:** **Python, Selenium, Pandas, Power BI.**
* **Código:** El código utilizado para la extracción y limpieza de datos está disponible en este repositorio, en la carpeta `src`.


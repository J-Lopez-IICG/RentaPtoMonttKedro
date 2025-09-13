Análisis de Mercado de Arriendos en Puerto Montt

Resumen del Proyecto

Este proyecto se desarrolló para abordar el problema de la falta de datos estructurados en el mercado de arriendos de Puerto Montt. El objetivo principal fue obtener, limpiar y analizar datos de propiedades para identificar las mejores opciones de arriendo y ofrecer una visión clara de las dinámicas del mercado inmobiliario. El análisis culminó en un dashboard interactivo en Power BI que permite a los usuarios tomar decisiones informadas sobre dónde y qué tipo de propiedad arrendar.

Proceso de Análisis

El proyecto siguió un ciclo de vida de análisis de datos de principio a fin:
Extracción de datos: Se creó un script en Python utilizando la librería Selenium para automatizar la extracción de datos de un sitio web de bienes raíces. Este script fue diseñado para superar desafíos como la paginación y la estructura cambiante del sitio, obteniendo información sobre más de 300 arriendos.
Limpieza y transformación: Los datos extraídos fueron procesados en Power Query. Se realizaron transformaciones clave como la conversión de precios de UF a pesos chilenos, la estandarización de la cantidad de dormitorios y baños, y el manejo de valores faltantes.
Análisis y visualización: En Power BI, se construyeron medidas clave (KPIs) y se crearon visualizaciones interactivas para explorar el conjunto de datos y presentar los hallazgos de forma clara.

Hallazgos Clave

El análisis de los datos reveló varias tendencias importantes del mercado:
Precio por m²: El precio promedio por metro cuadrado de los arriendos es de 2.445 mil pesos, lo que sirve como un punto de referencia para comparar la eficiencia de diferentes propiedades.
Correlación de precios: Se identificó una fuerte correlación positiva entre el tamaño de la propiedad (en metros cuadrados) y el precio de arriendo.
Comparativa de propiedades: A pesar de que las casas tienen un precio de arriendo promedio más alto, el análisis reveló que los departamentos son significativamente más caros por metro cuadrado. Este hallazgo es crucial para los usuarios que buscan maximizar el espacio por su inversión.
Valores atípicos: Se identificaron y analizaron valores atípicos, como arriendos de terrenos o bodegas, que distorsionaban el análisis. Estos datos fueron manejados para asegurar que las conclusiones se basaran en la información más relevante para el usuario final.

Código y Herramientas

Herramientas: Python, Selenium, Pandas, Power BI.
Código: El código utilizado para la extracción y limpieza de datos está disponible en mi perfil de GitHub.


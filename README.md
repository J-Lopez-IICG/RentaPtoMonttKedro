# RentaPtoMonttKedro

[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)

## Visión General

Este proyecto Kedro está diseñado para automatizar la extracción, limpieza y transformación de datos de arriendos inmobiliarios en Puerto Montt, Chile. La información se obtiene mediante web scraping de PortalInmobiliario.com y se procesa para generar un dataset estructurado y limpio, listo para ser consumido por herramientas de Business Intelligence como Power BI, facilitando así un análisis detallado del mercado de arriendos.

El proyecto utiliza el framework modular y reproducible de Kedro para asegurar la calidad de los datos y la fiabilidad del pipeline.

## Estructura del Proyecto

El proyecto se organiza en los siguientes pipelines principales:

*   **`data_engineering`**: Encargado del web scraping de las publicaciones de arriendo de PortalInmobiliario.com, gestionando la paginación y almacenando los datos en su formato crudo (`data/01_raw/arriendos_puerto_montt.xlsx`).
*   **`data_processing`**: Se enfoca en la limpieza y transformación de los datos crudos. Esto incluye:
    *   Obtención del valor actual de la UF (Unidad de Fomento) desde una API externa.
    *   Conversión de precios de UF a CLP (Pesos Chilenos).
    *   Extracción y estandarización de atributos de las propiedades (ej. dormitorios, baños, superficie en m2).
    *   Normalización de columnas de texto (ej. título, ubicación, tipo de hogar).
    *   Selección de las columnas finales y eliminación de registros con valores nulos o inconsistentes en el precio.

El resultado final de este pipeline es un dataset limpio y estructurado (`data/02_intermediate/arriendos_puerto_montt_processed.xlsx`) listo para el análisis y la visualización.

### Carpeta `notebooks`

La carpeta `notebooks` contiene los Jupyter Notebooks utilizados durante la fase de desarrollo y exploración de datos. Estos notebooks sirven como un "laboratorio" interactivo para probar ideas, depurar funciones y documentar el proceso de diseño de los nodos del pipeline.

**Para que un tercero pueda ver tus notebooks**, simplemente necesita clonar este repositorio de Git. Los archivos `.ipynb` son parte del código fuente del proyecto y se comparten como cualquier otro archivo. No son ejecutados directamente por el pipeline de Kedro, sino que son recursos de desarrollo y documentación.

## Resultados y Visualización

El dataset final procesado (`data/02_intermediate/arriendos_puerto_montt_processed.xlsx`) se utiliza como fuente de datos para un dashboard interactivo en Power BI, el cual permite un análisis detallado del mercado de arriendos en Puerto Montt.

### Principales Hallazgos del Dashboard

El análisis visual de los datos revela varias tendencias clave en el mercado inmobiliario de la ciudad:

*   **Volumen de Datos:** Se procesaron inicialmente cerca de 600 registros, filtrando por arrendamientos de casas y departamentos para obtener un conjunto de datos final de **329 publicaciones** para el análisis.
*   **Precio por Metro Cuadrado:** El m² de una **casa es notablemente más económico que el de un departamento**. Aunque el arriendo promedio de un departamento es más bajo, este ofrece una superficie mucho menor, posicionando a las casas como una opción más rentable en términos de espacio/precio.
*   **Impacto de los Dormitorios en el Precio:** Se observa que el precio de arriendo tiende a disminuir en propiedades que superan los **3 dormitorios**.
*   **Distribución de Baños:** Las propiedades con **2 baños** dominan el mercado, siendo significativamente más numerosas que las que cuentan con 3 baños.

Puedes explorar el dashboard interactivo para un análisis más profundo y filtrar los datos según tus intereses:

[Dashboard de Arriendos Puerto Montt en Power BI](https://app.powerbi.com/view?r=eyJrIjoiYWNmMDJkYWMtNzQzYy00Y2Y1LWIwY2QtYmVkYTVhODYzMWZkIiwidCI6ImRmNGI2MzcyLWEwM2EtNDZmMC05YmY1LTdmOGQzNzhhMzMzNCIsImMiOjR9)

## Reglas y Directrices

Para aprovechar al máximo esta plantilla:

*   No elimines ninguna línea del archivo `.gitignore` que proporcionamos.
*   Asegúrate de que tus resultados puedan ser reproducidos siguiendo una convención de ingeniería de datos.
*   No subas datos a tu repositorio.
*   No subas ninguna credencial o tu configuración local a tu repositorio. Mantén todas tus credenciales y configuración local en `conf/local/`.

## Cómo instalar dependencias

Declara cualquier dependencia en `requirements.txt` para la instalación con `pip`.

Para instalarlas, ejecuta:

```bash
pip install -r requirements.txt
```

## Cómo ejecutar tu pipeline Kedro

Puedes ejecutar tu proyecto Kedro con:

```bash
kedro run
```

## Dependencias del Proyecto

Para ver y actualizar los requisitos de dependencia de tu proyecto, usa `requirements.txt`. Puedes instalar los requisitos del proyecto con `pip install -r requirements.txt`.

[Más información sobre las dependencias del proyecto](https://docs.kedro.org/en/stable/kedro_project_setup/dependencies.html#project-specific-dependencies)

## Cómo trabajar con Kedro y notebooks

> Nota: Usar `kedro jupyter` o `kedro ipython` para ejecutar tu notebook proporciona estas variables en el ámbito: `context`, `session`, `catalog` y `pipelines`.
>
> Jupyter, JupyterLab e IPython ya están incluidos en los requisitos del proyecto por defecto, así que una vez que hayas ejecutado `pip install -r requirements.txt` no necesitarás realizar ningún paso adicional antes de usarlos.
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

## Resultados y Visualización

El dataset final procesado se utiliza como fuente de datos para un dashboard interactivo en Power BI.

[**Ver Dashboard de Arriendos Puerto Montt en Power BI**](https://app.powerbi.com/view?r=eyJrIjoiYWNmMDJkYWMtNzQzYy00Y2Y1LWIwY2QtYmVkYTVhODYzMWZkIiwidCI6ImRmNGI2MzcyLWEwM2EtNDZmMC05YmY1LTdmOGQzNzhhMzMzNCIsImMiOjR9)

### Principales Hallazgos del Dashboard

*   **Volumen de Datos:** Se procesaron inicialmente cerca de 600 registros, filtrando por arrendamientos de casas y departamentos para obtener un conjunto de datos final de **329 publicaciones** para el análisis.
*   **Precio por Metro Cuadrado:** El m² de una **casa es notablemente más económico que el de un departamento**. Aunque el arriendo promedio de un departamento es más bajo, este ofrece una superficie mucho menor, posicionando a las casas como una opción más rentable en términos de espacio/precio.
*   **Impacto de los Dormitorios en el Precio:** Se observa que el precio de arriendo tiende a disminuir en propiedades que superan los **3 dormitorios**.
*   **Distribución de Baños:** Las propiedades con **2 baños** dominan el mercado, siendo significativamente más numerosas que las que cuentan con 3 baños.

---

## Instalación y Ejecución

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local.

### 1. Clonar el Repositorio

Primero, clona este repositorio en tu máquina.

```bash
git clone https://github.com/J-Lopez-IICG/RentaPtoMonttWebScrapingPython-DashbPowerBi.git
cd RentaPtoMonttWebScrapingPython-DashbPowerBi
```

### 2. Crear y Activar un Entorno Virtual

Es una práctica recomendada utilizar un entorno virtual para aislar las dependencias de este proyecto y evitar conflictos con otros proyectos de Python en tu sistema.

```bash
# Crear el entorno virtual
python -m venv venv

# Activar en Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Activar en macOS/Linux
# source venv/bin/activate
```

### 3. Instalar Dependencias

Una vez que el entorno virtual esté activado, instala todas las librerías necesarias, incluyendo Kedro, con el siguiente comando.

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el Pipeline

Con las dependencias instaladas, puedes ejecutar el pipeline completo con un solo comando.

```bash
kedro run
```

Esto ejecutará todos los nodos en secuencia y generará el dataset final en `data/02_intermediate/`.

---

## Desarrollo con Notebooks

La carpeta `notebooks` contiene los Jupyter Notebooks utilizados durante la fase de exploración y desarrollo.

Para trabajar con ellos de forma interactiva dentro del contexto de Kedro, ejecuta:

```bash
kedro jupyter lab
# o también
kedro jupyter notebook
```

> **Nota**: Al usar estos comandos, Kedro inicia el notebook con las variables `context`, `session`, `catalog` y `pipelines` ya cargadas, facilitando la interacción con los datos y funciones del proyecto.

## Reglas y Directrices

*   No elimines ninguna línea del archivo `.gitignore`.
*   No subas datos al repositorio (la carpeta `data/` está ignorada por defecto).
*   No subas credenciales o configuraciones locales. Mantenlas en la carpeta `conf/local/`.
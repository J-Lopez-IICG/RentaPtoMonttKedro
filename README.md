# RentaPtoMonttKedro

[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)

## Visión General

Este proyecto Kedro automatiza un pipeline de datos para analizar el mercado de arriendos inmobiliarios en Puerto Montt, Chile. La solución ingiere y combina información de dos fuentes clave: realiza web scraping en PortalInmobiliario.com para obtener los listados de propiedades y consume una API financiera para obtener el valor diario de la Unidad de Fomento (UF).

Durante la fase de transformación, el pipeline limpia y enriquece los datos, convirtiendo los precios a una moneda estándar para facilitar la comparación. El resultado es un dataset consolidado y listo para ser consumido por herramientas de Business Intelligence como Power BI, permitiendo un análisis preciso y financieramente relevante del mercado local.

---

## Estructura del Proyecto

El proyecto se organiza en los siguientes pipelines principales:

* **`data_engineering`**: Encargado del web scraping de las publicaciones de arriendo de PortalInmobiliario.com, gestionando la paginación y almacenando los datos en su formato crudo (`data/01_raw/arriendos_puerto_montt.xlsx`).
* **`data_processing`**: Se enfoca en la limpieza y transformación de los datos crudos. Esto incluye:
    * Obtención del valor actual de la UF (Unidad de Fomento) desde una API externa.
    * Conversión de precios de UF a CLP (Pesos Chilenos).
    * Extracción y estandarización de atributos de las propiedades (ej. dormitorios, baños, superficie en m²).
    * Normalización de columnas de texto (ej. título, ubicación, tipo de hogar).
    * Selección de las columnas finales y eliminación de registros con valores nulos o inconsistentes.

El resultado final de este pipeline es un dataset limpio y estructurado (`data/02_intermediate/arriendos_puerto_montt_processed.xlsx`) listo para el análisis.

---

## Resultados y Visualización

El dataset final procesado se utiliza como fuente de datos para un dashboard interactivo en Power BI.

[**Ver Dashboard de Arriendos Puerto Montt en Power BI: Renta Puerto Montt**](https://app.powerbi.com/view?r=eyJrIjoiYWNmMDJkYWMtNzQzYy00Y2Y1LWIwY2QtYmVkYTVhODYzMWZkIiwidCI6ImRmNGI2MzcyLWEwM2EtNDZmMC05YmY1LTdmOGQzNzhhMzMzNCIsImMiOjR9)

### Principales Hallazgos del Dashboard

* **Volumen de Datos:** Se procesaron inicialmente cerca de 600 registros, filtrando por casas y departamentos para obtener un conjunto final de **329 publicaciones** para el análisis.
* **Precio por Metro Cuadrado:** El m² de una **casa es notablemente más económico que el de un departamento**. Aunque el arriendo promedio de un departamento es más bajo, este ofrece menos superficie, posicionando a las casas como una opción más rentable en términos de espacio/precio.
* **Impacto de los Dormitorios en el Precio:** Se observa que el precio de arriendo tiende a disminuir en propiedades que superan los **3 dormitorios**.
* **Distribución de Baños:** Las propiedades con **2 baños** dominan el mercado, siendo significativamente más numerosas que las que cuentan con 3 o más baños.

### Desafíos Técnicos Solucionados

* **Scraping Robusto y Anti-Bloqueo**: Para superar las medidas de seguridad de PortalInmobiliario.com, el scraper fue diseñado para simular comportamiento humano, usando `User-Agents` y pausas estratégicas entre peticiones. Se implementó también una lógica robusta para navegar la paginación del sitio y recopilar todos los listados.

* **Extracción y Estandarización de Atributos**: Se utilizaron expresiones regulares (regex) para extraer valores numéricos de texto no estructurado (ej. "3 dormitorios", "120 m²"), convirtiendo datos cualitativos en cuantitativos y listos para el análisis.

* **Normalización de Precios (UF y CLP)**: Se integró una API financiera para obtener el valor diario de la UF y se desarrolló una lógica condicional para identificar la moneda de cada publicación y convertir todos los precios a una unidad común, permitiendo una comparación precisa.

* **Manejo de Datos Inconsistentes**: Se implementaron pasos de validación para convertir precios a formato numérico y eliminar sistemáticamente registros con valores nulos o inválidos, garantizando la fiabilidad del dataset final.

---

## Instalación y Ejecución

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local.

### 1. Clonar el Repositorio

Primero, clona este repositorio en tu máquina.

```bash
git clone https://github.com/J-Lopez-IICG/RentaPtoMonttKedro.git
cd RentaPtoMonttKedro
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

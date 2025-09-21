# RentaPtoMonttKedro

[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)

## Overview

Este proyecto Kedro está diseñado para automatizar la extracción, limpieza y transformación de datos de arriendos inmobiliarios en Puerto Montt, Chile. La información se obtiene mediante web scraping de PortalInmobiliario.com y se procesa para generar un dataset estructurado y limpio, listo para ser consumido por herramientas de Business Intelligence como Power BI, facilitando así un análisis detallado del mercado de arriendos.

El proyecto utiliza el framework modular y reproducible de Kedro para asegurar la calidad de los datos y la fiabilidad del pipeline.

## Project Structure

El proyecto se organiza en los siguientes pipelines principales:

*   **`data_engineering`**: Encargado del web scraping de las publicaciones de arriendo de PortalInmobiliario.com, gestionando la paginación y almacenando los datos en su formato crudo (`data/01_raw/arriendos_puerto_montt.xlsx`).
*   **`data_processing`**: Se enfoca en la limpieza y transformación de los datos crudos. Esto incluye:
    *   Obtención del valor actual de la UF (Unidad de Fomento) desde una API externa.
    *   Conversión de precios de UF a CLP (Pesos Chilenos).
    *   Extracción y estandarización de atributos de las propiedades (ej. dormitorios, baños, superficie en m2).
    *   Normalización de columnas de texto (ej. título, ubicación, tipo de hogar).
    *   Selección de las columnas finales y eliminación de registros con valores nulos o inconsistentes en el precio.

El resultado final es un dataset limpio y estructurado (`data/02_intermediate/arriendos_puerto_montt_processed.xlsx`) listo para el análisis y la visualización.

## Rules and guidelines

In order to get the best out of the template:

*   Don't remove any lines from the `.gitignore` file we provide
*   Make sure your results can be reproduced by following a data engineering convention
*   Don't commit data to your repository
*   Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/`

## How to install dependencies

Declare any dependencies in `requirements.txt` for `pip` installation.

To install them, run:

```bash
pip install -r requirements.txt
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```bash
kedro run
```

## How to test your Kedro project

Have a look at the file `tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```bash
pytest
```

You can configure the coverage threshold in your project's `pyproject.toml` file under the `[tool.coverage.report]` section.


## Project dependencies

To see and update the dependency requirements for your project use `requirements.txt`. You can install the project requirements with `pip install -r requirements.txt`.

[Further information about project dependencies](https://docs.kedro.org/en/stable/kedro_project_setup/dependencies.html#project-specific-dependencies)

## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `context`, 'session', `catalog`, and `pipelines`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `pip install -r requirements.txt` you will not need to take any extra steps before you use them.

### Jupyter
To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

```bash
pip install jupyter
```

After installing Jupyter, you can start a local notebook server:

```bash
kedro jupyter notebook
```

### JupyterLab
To use JupyterLab, you need to install it:

```bash
pip install jupyterlab
```

You can also start JupyterLab:

```bash
kedro jupyter lab
```

### IPython
And if you want to run an IPython session:

```bash
kedro ipython
```

### How to ignore notebook output cells in `git`
To automatically strip out all output cell contents before committing to `git`, you can use tools like [`nbstripout`](https://github.com/kynan/nbstripout). For example, you can add a hook in `.git/config` with `nbstripout --install`. This will run `nbstripout` before anything is committed to `git`.

> *Note:* Your output cells will be retained locally.

## Package your Kedro project

[Further information about building project documentation and packaging your project](https://docs.kedro.org/en/stable/tutorial/package_a_project.html)
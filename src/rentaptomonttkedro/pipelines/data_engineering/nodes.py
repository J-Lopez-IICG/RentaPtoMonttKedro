# filepath: src/renta_pto_montt_kedro/pipelines/data_engineering/nodes.py
"""
Este es el pipeline para la extracción y limpieza de datos.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from requests.exceptions import ConnectionError
import time
import pandas as pd
import os
from unidecode import unidecode


def _setup_driver() -> webdriver.Edge:
    """Configura el WebDriver de forma inteligente, con respaldo manual."""
    driver = None
    try:
        print("Intentando configurar WebDriver automáticamente...")
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
        print("WebDriver configurado automáticamente.")
    except ConnectionError:
        print("\nFalló la configuración automática. Intentando desde ruta local...")

        # La ruta ahora se construye desde la raíz del proyecto Kedro
        driver_path = os.path.join("driver", "msedgedriver.exe")

        if os.path.exists(driver_path):
            service = EdgeService(executable_path=driver_path)
            driver = webdriver.Edge(service=service)
            print(f"WebDriver configurado manualmente desde: {driver_path}")
        else:
            raise FileNotFoundError(
                f"No se pudo encontrar el driver manual en {driver_path}"
            )

    if not driver:
        raise Exception("No se pudo inicializar el driver por ningún método.")

    return driver


def scrape_raw_data() -> pd.DataFrame:
    """
    Realiza el web scraping del sitio de arriendos y devuelve los datos
    en un DataFrame de pandas.
    """
    driver = _setup_driver()

    all_posts = []
    error_count = 0
    offset = 1

    while True:
        url = f"https://www.portalinmobiliario.com/arriendo/puerto-montt-los-lagos/_Desde_{offset}_NoIndex_True_number%7D_True"
        driver.get(url)
        time.sleep(5)

        try:
            posts = driver.find_elements(By.CLASS_NAME, "poly-card__content")
            if not posts:
                print("No se encontraron más publicaciones. Terminando el proceso.")
                break

            print(
                f"Procesando {len(posts)} publicaciones de la página con offset {offset}..."
            )

            for post in posts:
                try:
                    post_data = {
                        "Tipo_de_hogar": unidecode(
                            post.find_element(By.CLASS_NAME, "poly-component__headline").text
                        ),
                        "Precio": unidecode(
                            post.find_element(By.CLASS_NAME, "poly-component__price").text
                        ),
                        "Atributos": unidecode(
                            post.find_element(
                                By.CLASS_NAME, "poly-component__attributes-list"
                            ).text
                        ),
                        "Ubicacion": unidecode(
                            post.find_element(By.CLASS_NAME, "poly-component__location").text
                        ),
                    }
                    all_posts.append(post_data)
                except Exception:
                    error_count += 1
                    pass

            offset += 48

        except Exception as e:
            print(f"Ocurrió un error en la página con offset {offset}: {e}")
            break

    driver.quit()

    print("\n--- Extracción finalizada ---")
    print(f"Total de publicaciones extraídas: {len(all_posts)}")
    print(f"Total de publicaciones con error (omitidas): {error_count}")

    df = pd.DataFrame(all_posts)
    return df

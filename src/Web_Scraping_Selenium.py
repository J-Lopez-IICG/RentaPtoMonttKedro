from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from requests.exceptions import ConnectionError
import time
import pandas as pd
import os
from unidecode import unidecode

# --- Configuración Inteligente del WebDriver ---
driver = None
try:
    # --- MÉTODO 1: Automático (Ideal para reproducibilidad) ---
    print("Intentando configurar WebDriver automáticamente...")
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    print("WebDriver configurado automáticamente.")

except ConnectionError:
    # --- MÉTODO 2: Manual (Como respaldo si falla la conexión a internet) ---
    print("\nFalló la configuración automática por un problema de red.")
    print("Intentando configurar WebDriver desde una ruta local...")

    # Construye la ruta relativa al driver dentro del proyecto
    script_dir = os.path.dirname(__file__)
    project_root = os.path.dirname(script_dir)
    driver_path = os.path.join(project_root, "driver", "msedgedriver.exe")

    if os.path.exists(driver_path):
        service = EdgeService(executable_path=driver_path)
        driver = webdriver.Edge(service=service)
        print(f"WebDriver configurado manualmente desde: {driver_path}")
    else:
        print("\n--- ERROR CRÍTICO ---")
        print("No se pudo configurar el WebDriver.")
        print("1. La descarga automática falló por un problema de red.")
        print(f"2. No se encontró el driver manual en la ruta esperada: {driver_path}")
        print(
            "\nSOLUCIÓN: Descargue 'msedgedriver.exe' y colóquelo en la carpeta 'driver' en la raíz del proyecto."
        )

# Si el driver no se pudo inicializar por ningún método, detenemos el script.
if not driver:
    print("No se pudo inicializar el driver. Abortando ejecución.")
    exit()

all_posts = []
offset = 1  # El primer resultado en la página

while True:
    url = f"https://www.portalinmobiliario.com/arriendo/puerto-montt-los-lagos/_Desde_{offset}_NoIndex_True"

    print(f"Extrayendo datos desde el resultado número: {offset}")
    driver.get(url)
    time.sleep(3)

    try:
        posts = driver.find_elements(By.CLASS_NAME, "poly-card__content")

        # Si no se encuentran publicaciones, significa que llegamos al final.
        if not posts:
            print("No se encontraron más publicaciones. Terminando el proceso.")
            break

        for post in posts:
            try:
                # --- 2. Aplicamos unidecode para limpiar el texto extraído ---
                title = unidecode(
                    post.find_element(
                        By.CLASS_NAME, "poly-component__title-wrapper"
                    ).text.replace("\n", " ")
                )
                type_of_home = unidecode(
                    post.find_element(
                        By.CLASS_NAME, "poly-component__headline"
                    ).text.replace("\n", " ")
                )
                price = unidecode(
                    post.find_element(
                        By.CLASS_NAME, "poly-component__price"
                    ).text.replace("\n", " ")
                )
                location = unidecode(
                    post.find_element(
                        By.CLASS_NAME, "poly-component__location"
                    ).text.replace("\n", " ")
                )
                attributes = unidecode(
                    post.find_element(
                        By.CLASS_NAME, "poly-component__attributes-list"
                    ).text.replace("\n", " ")
                )

                post_data = {
                    "Tipo_de_hogar": type_of_home,
                    "Titulo": title,
                    "Precio": price,
                    "Ubicacion": location,
                    "Atributos": attributes,
                }

                all_posts.append(post_data)

            except Exception:
                # Si un post individual falla, lo saltamos y continuamos con el siguiente.
                pass

        # Avanzamos al siguiente grupo de resultados
        offset += 48

    except Exception as e:
        print(f"Ocurrió un error irrecuperable en la página con offset {offset}: {e}")
        break

driver.quit()

print("\n--- Extracción finalizada ---")

print(f"Total de publicaciones extraídas: {len(all_posts)}")


if all_posts:
    df = pd.DataFrame(all_posts)

    directorio = r"C:\Users\javie\Documents\GitHub\RentaPtoMonttWebScrapingPython-DashbPowerBi\data"
    # --- 3. Cambiamos el nombre del archivo a .xlsx ---
    nombre_archivo = "arriendos_puerto_montt.xlsx"

    ruta_completa = os.path.join(directorio, nombre_archivo)

    os.makedirs(directorio, exist_ok=True)

    try:
        # --- 4. Usamos to_excel() para guardar el archivo ---
        df.to_excel(ruta_completa, index=False)
        print(f"Datos guardados exitosamente como Excel en:\n'{ruta_completa}'")

    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo: {e}")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time
import pandas as pd

# Reemplaza con la ruta real a tu msedgedriver.exe
driver_path = 'C:/Users/javie/Documents/edgedriver_win64/msedgedriver.exe'
service = Service(executable_path=driver_path)

# Inicializa el navegador Edge
driver = webdriver.Edge(service=service)

all_posts = []

for page_number in range(0, 700, 48):
    url = f"https://www.portalinmobiliario.com/arriendo/puerto-montt-los-lagos/_Desde_{page_number}_NoIndex_True"
    
    print(f"Extrayendo datos de la página con el número de inicio: {page_number}")
    driver.get(url)
    time.sleep(3) 

    try:
        posts = driver.find_elements(By.CLASS_NAME, "poly-card__content")

        if not posts:
            print(f"No se encontraron publicaciones en la página {page_number}. Terminando el proceso.")
            break

        for post in posts:
            try:
                title = post.find_element(By.CLASS_NAME, "poly-component__title-wrapper").text.replace('\n', ' ')
                type_of_home = post.find_element(By.CLASS_NAME, "poly-component__headline").text.replace('\n', ' ')
                price = post.find_element(By.CLASS_NAME, "poly-component__price").text.replace('\n', ' ')
                location = post.find_element(By.CLASS_NAME, "poly-component__location").text.replace('\n', ' ')
                attributes = post.find_element(By.CLASS_NAME, "poly-component__attributes-list").text.replace('\n', ' ')
                post_data = {
                    "Tipo_de_hogar": type_of_home,
                    "Titulo": title,
                    "Precio": price,
                    "Ubicacion": location,
                    "Atributos": attributes
                }
                
                all_posts.append(post_data)

            except Exception:
                pass

    except Exception as e:
        print(f"Ocurrió un error en la página {page_number}: {e}")
        break

driver.quit()

print("\n--- Extracción finalizada ---")
print(f"Total de publicaciones extraídas: {len(all_posts)}")

if all_posts:
    df = pd.DataFrame(all_posts)
    try:
        df.to_csv('arriendos_puerto_montt.csv', index=False, sep='-')
        print("Datos guardados exitosamente en 'arriendos_puerto_montt.csv'")
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo: {e}")

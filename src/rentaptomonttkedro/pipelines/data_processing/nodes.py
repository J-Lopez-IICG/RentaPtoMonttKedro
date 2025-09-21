import pandas as pd
import requests # Necesario para la API de UF
from datetime import datetime # Necesario para la API de UF
from typing import Dict # Útil para tipado, aunque no se use directamente en estas funciones

def get_current_uf_value() -> float:
    """
    Obtiene el valor actual de la UF usando la API de mindicador.cl.
    Devuelve solo el valor de la UF como un float.
    """
    url = "https://mindicador.cl/api/uf"
    print("Obteniendo el valor actual de la UF desde mindicador.cl...")

    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error si la solicitud no fue exitosa

        data = response.json()

        if "serie" in data and len(data["serie"]) > 0:
            ultima_observacion = data["serie"][0]
            fecha_valor = datetime.strptime(
                ultima_observacion["fecha"], "%Y-%m-%dT%H:%M:%S.%fZ"
            )
            valor_uf = ultima_observacion["valor"]
            print(f"UF obtenida al {fecha_valor.strftime('%d-%m-%Y')} es: ${valor_uf:,.2f} pesos.")
            return valor_uf
        else:
            print("No se encontraron datos de UF en la respuesta de la API. Usando valor fijo de respaldo.")
            return 38000.0 # Valor fijo de respaldo si la API no devuelve datos

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión a la API: {e}. Usando valor fijo de respaldo.")
        return 38000.0 # Valor fijo de respaldo en caso de error de conexión
    except Exception as e:
        print(f"Error al procesar la respuesta de la API: {e}. Usando valor fijo de respaldo.")
        return 38000.0 # Valor fijo de respaldo en caso de otro error


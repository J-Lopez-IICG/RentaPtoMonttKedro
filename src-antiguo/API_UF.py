import requests
import json
from datetime import datetime


def get_uf_from_mindicador():
    """
    Obtiene el valor actual de la UF usando la API de mindicador.cl.
    """
    url = "https://mindicador.cl/api/uf"

    try:
        # Realiza la solicitud HTTP GET
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error si la solicitud no fue exitosa

        data = response.json()

        # El valor de la UF más reciente está en la primera entrada de la lista
        if "serie" in data and len(data["serie"]) > 0:
            ultima_observacion = data["serie"][0]
            fecha_valor = datetime.strptime(
                ultima_observacion["fecha"], "%Y-%m-%dT%H:%M:%S.%fZ"
            )
            valor_uf = ultima_observacion["valor"]

            return fecha_valor, valor_uf

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión a la API: {e}")
        return None, None
    except Exception as e:
        print(f"Error al procesar la respuesta de la API: {e}")
        return None, None


if __name__ == "__main__":
    fecha, uf_valor = get_uf_from_mindicador()

    if uf_valor:
        print(
            f"El valor actual de la UF al {fecha.strftime('%d-%m-%Y')} es: ${uf_valor:,.2f} pesos."
        )
    else:
        print("No se pudo obtener el valor de la UF de la API.")

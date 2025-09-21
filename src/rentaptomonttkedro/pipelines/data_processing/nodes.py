import pandas as pd
import numpy as np # Necesario para np.nan
import re # Necesario para expresiones regulares
import requests # Necesario para la API de UF
from datetime import datetime
from typing import Dict
from unidecode import unidecode # Necesario para limpiar texto

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


def convert_prices_to_clp(df: pd.DataFrame, uf_value: float) -> pd.DataFrame:
    """
    Limpia la columna 'Precio', la convierte a CLP si es UF, y crea 'Precio_CLP'.
    """
    df_processed = df.copy()

    def _clean_price_single_value(price_str, uf_value_local):
        """
        Función auxiliar para limpiar un solo valor de precio.
        Adaptada de tu función clean_price del Jupyter.
        """
        price_str = str(price_str).strip()

        # Caso 1: Precio en UF
        if "uf" in price_str.lower():
            numbers = re.findall(r"(\d+\.?\d*)", price_str)
            if numbers:
                try:
                    numeric_values = [float(n) for n in numbers]
                    uf_price_avg = sum(numeric_values) / len(numeric_values)
                    return round(uf_price_avg * uf_value_local)
                except (ValueError, ZeroDivisionError):
                    return np.nan
            return np.nan
        
        # Caso 2: Precio en CLP
        else:
            numbers_only = re.sub(r"\D", "", price_str)
            if numbers_only:
                try:
                    return int(numbers_only)
                except ValueError:
                    return np.nan
            return np.nan

    # Aplicamos la función auxiliar a la columna 'Precio'
    df_processed['Precio_CLP'] = df_processed['Precio'].apply(lambda x: _clean_price_single_value(x, uf_value))

    return df_processed


def limpiar_y_separar_atributos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Toma el DataFrame y extrae 'Dormitorios', 'Banos', 'Superficie_m2', 'Privados'
    de la columna 'Atributos'.
    """
    df_processed = df.copy()

    df_processed['Atributos'] = df_processed['Atributos'].astype(str)

    # Usamos expresiones regulares para extraer la información de la columna 'Atributos'
    df_processed['Dormitorios'] = df_processed['Atributos'].str.extract(r'(\d+)\s*dormitorio', flags=re.IGNORECASE, expand=False).fillna(0)
    df_processed['Banos'] = df_processed['Atributos'].str.extract(r'(\d+)\s*bano', flags=re.IGNORECASE, expand=False).fillna(0)
    df_processed['Superficie_m2'] = df_processed['Atributos'].str.extract(r'(\d+)\s*m2', flags=re.IGNORECASE, expand=False).fillna(0)
    df_processed['Privados'] = df_processed['Atributos'].str.extract(r'(\d+)\s*privado', flags=re.IGNORECASE, expand=False).fillna(0)

    # Convertimos las nuevas columnas a tipo numérico (entero)
    df_processed[['Dormitorios', 'Banos', 'Superficie_m2', 'Privados']] = df_processed[['Dormitorios', 'Banos', 'Superficie_m2', 'Privados']].astype(int)

    return df_processed


def clean_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normaliza las columnas de texto principales (Titulo, Ubicacion, Tipo_de_hogar)
    eliminando tildes, caracteres especiales y estandarizando el contenido.
    """
    df_processed = df.copy()

    # Normalizamos texto: quitamos tildes y caracteres especiales
    for col in ['Titulo', 'Ubicacion', 'Tipo_de_hogar']:
        if col in df_processed.columns:
            df_processed[col] = df_processed[col].apply(lambda x: unidecode(str(x)))

    # Estandarizamos la columna 'Tipo_de_hogar'
    if 'Tipo_de_hogar' in df_processed.columns:
        df_processed['Tipo_de_hogar'] = df_processed['Tipo_de_hogar'].str.replace(" en arriendo", "", case=False).str.strip()

    return df_processed


def select_and_clean_final_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Selecciona las columnas finales deseadas y elimina filas con precios nulos o cero.
    """
    df_final = df.copy()

    # Definimos las columnas que queremos en nuestro dataset final
    columnas_finales = [
        'Tipo_de_hogar',
        'Precio', # Mantener la columna original de precio si es útil para referencia
        'Moneda', # Mantener la columna de moneda para referencia
        'Atributos', # Mantener la columna original de atributos si es útil para referencia
        'Ubicacion',
        'Link', # Asegurarse de incluir el link si se extrajo
        'Precio_CLP',
        'Dormitorios',
        'Banos',
        'Privados',
        'Superficie_m2'
    ]
    
    # Filtrar solo las columnas que realmente existen en el DataFrame
    existing_columns = [col for col in columnas_finales if col in df_final.columns]
    df_final = df_final[existing_columns].copy()

    # Eliminamos filas donde no se pudo calcular el precio en CLP o es cero
    df_final.dropna(subset=['Precio_CLP'], inplace=True)
    df_final = df_final[df_final['Precio_CLP'] > 0]

    # Opcional: Convertir tipos de datos a los más eficientes
    df_final = df_final.convert_dtypes()

    return df_final
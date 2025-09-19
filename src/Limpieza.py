# Contenido para tu script principal de limpieza de datos
# Limpieza.py

import pandas as pd
import numpy as np
import re
import os
from API_UF import get_uf_from_mindicador 
from unidecode import unidecode

# --- 1. Configuración de Archivos ---
input_path = r'C:\Users\javie\Documents\GitHub\RentaPtoMonttWebScrapingPython-DashbPowerBi\data\arriendos_puerto_montt.xlsx'
output_path = r'C:\Users\javie\Documents\GitHub\RentaPtoMonttWebScrapingPython-DashbPowerBi\data\arriendos_puerto_montt_limpio.xlsx'

# --- 2. Cargar los Datos ---
try:
    df = pd.read_excel(input_path)
    print("Archivo Excel cargado exitosamente.")
except FileNotFoundError:
    print(f"Error: No se encontró el archivo en la ruta '{input_path}'.")
    exit()
except Exception as e:
    print(f"Ocurrió un error al cargar el archivo: {e}")
    exit()

# --- 3. Obtener el Valor de la UF ---
print("Obteniendo valor de la UF...")
fecha, uf_actual = get_uf_from_mindicador()

if uf_actual:
    uf_actual = float(uf_actual)
    print(f"Valor de la UF para el {fecha}: ${uf_actual:,.2f}")
else:
    uf_actual = 40000 
    print(f"Advertencia: No se pudo obtener la UF. Se usará un valor por defecto de ${uf_actual:,.0f}")

# --- 4. Limpieza y Transformación ---
print("\nIniciando limpieza y transformación de datos...")

def clean_price(price_str, uf_value):
    price_str = str(price_str).strip()
    
    if 'uf' in price_str.lower():
        numbers = re.findall(r'(\d+)', price_str)
        if numbers:
            try:
                numeric_values = [float(n) for n in numbers]
                uf_price_avg = sum(numeric_values) / len(numeric_values)
                return round(uf_price_avg * uf_value)
            except (ValueError, ZeroDivisionError):
                return np.nan
        else:
            return np.nan
    else:
        numbers_only = re.sub(r'\D', '', price_str)
        if numbers_only:
            try:
                return int(numbers_only)
            except ValueError:
                return np.nan
        else:
            return np.nan

df['Precio_CLP'] = df['Precio'].apply(lambda x: clean_price(x, uf_actual))

for col in ['Titulo', 'Ubicacion', 'Tipo_de_hogar']:
    if col in df.columns:
        df[col] = df[col].apply(lambda x: unidecode(str(x)))


df['Tipo_de_hogar'] = df['Tipo_de_hogar'].str.replace(' en arriendo', '', case=False).str.strip()

df['Atributos'] = df['Atributos'].astype(str)
df['Dormitorios'] = df['Atributos'].str.extract(r'(\d+)\s*dormitorio', flags=re.IGNORECASE).fillna(0)
df['Banos'] = df['Atributos'].str.extract(r'(\d+)\s*bano', flags=re.IGNORECASE).fillna(0)
df['Superficie_m2'] = df['Atributos'].str.extract(r'(\d+)\s*m2', flags=re.IGNORECASE).fillna(0)
df['Privados'] = df['Atributos'].str.extract(r'(\d+)\s*privado', flags=re.IGNORECASE).fillna(0)

df[['Dormitorios', 'Banos', 'Superficie_m2', 'Privados']] = df[['Dormitorios', 'Banos', 'Superficie_m2', 'Privados']].astype(int)

columnas_finales = [
    'Tipo_de_hogar','Precio','Atributos','Ubicacion','Precio_CLP', 
    'Dormitorios', 'Banos','Privados','Superficie_m2'
]

for col in columnas_finales:
    if col not in df.columns:
        df[col] = 0

df_limpio = df[columnas_finales].copy()
df_limpio.dropna(subset=['Precio_CLP'], inplace=True)
df_limpio = df_limpio[df_limpio['Precio_CLP'] > 0]

print("Limpieza finalizada.")

# --- 5. Verificación Final de Tipos ---
print("\nConvirtiendo columnas a sus tipos de datos óptimos...")
df_limpio = df_limpio.convert_dtypes()

print("Tipos de datos finales:")
print(df_limpio.info())

# --- 6. Guardar el archivo limpio ---
try:
    df_limpio.to_excel(output_path, index=False)
    print(f"\n¡Éxito! Datos limpios y con formato correcto guardados en:\n'{output_path}'")
except Exception as e:
    print(f"Ocurrió un error al guardar el archivo: {e}")

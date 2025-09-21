# filepath: c:\Users\javie\Documents\GitHub\RentaPtoMonttWebScrapingPython-DashbPowerBi\src\rentaptomonttkedro\pipelines\data_processing\pipeline.py
from kedro.pipeline import Pipeline, node, pipeline
# Importa todas las funciones de nodos que vas a usar
from .nodes import (
    get_current_uf_value,
    convert_prices_to_clp,
    limpiar_y_separar_atributos,
    clean_text_columns,
    select_and_clean_final_columns,
)

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            # Nodo para obtener el valor de la UF
            node(
                func=get_current_uf_value,
                inputs=None,
                outputs="uf_value",
                name="get_uf_value_node",
            ),
            # Nodo para limpiar columnas de texto (Titulo, Ubicacion, Tipo_de_hogar)
            node(
                func=clean_text_columns,
                inputs="raw_arriendos", # Toma el DataFrame del scraper
                outputs="df_with_cleaned_text", # Salida intermedia
                name="clean_text_columns_node",
            ),
            # Nodo para separar atributos (Dormitorios, Banos, Superficie_m2, Privados)
            node(
                func=limpiar_y_separar_atributos,
                inputs="df_with_cleaned_text", # Toma el DF con texto limpio
                outputs="df_with_separated_attributes", # Salida intermedia
                name="separate_attributes_node",
            ),
            # Nodo para convertir precios a CLP
            node(
                func=convert_prices_to_clp,
                inputs=["df_with_separated_attributes", "uf_value"], # Toma el DF con atributos y la UF
                outputs="df_with_converted_prices", # Salida intermedia
                name="convert_prices_to_clp_node",
            ),
            # Nodo para la selección final de columnas y limpieza de nulos
            node(
                func=select_and_clean_final_columns,
                inputs="df_with_converted_prices", # Toma el DF con precios convertidos
                outputs="processed_arriendos", # Salida final del procesamiento
                name="select_and_clean_final_columns_node",
            ),
        ]
    )
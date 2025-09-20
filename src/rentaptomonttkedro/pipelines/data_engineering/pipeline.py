# filepath: src/rentaptomonttkedro/pipelines/data_engineering/pipeline.py
"""
Este es el pipeline para la extracción de datos.
"""
from kedro.pipeline import Pipeline, node, pipeline
from .nodes import scrape_raw_data # Asegúrate de importar scrape_raw_data, no scrape_arriendos

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=scrape_raw_data, # Llama a la función correcta
                inputs=None, # No se pasan inputs a scrape_raw_data
                outputs="raw_arriendos",
                name="scrape_raw_data_node", # Nombre del nodo actualizado
            )
        ]
    )

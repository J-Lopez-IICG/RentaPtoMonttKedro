# filepath: c:\Users\javie\Documents\GitHub\RentaPtoMonttWebScrapingPython-DashbPowerBi\src\rentaptomonttkedro\pipelines\data_processing\pipeline.py
from kedro.pipeline import Pipeline, node, pipeline
from .nodes import get_current_uf_value

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=get_current_uf_value,
                inputs=None,
                outputs="uf_value", # Salida: el valor de la UF
                name="get_uf_value_node",
            ),
        ]
    )
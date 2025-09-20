"""Project pipelines."""

from typing import Dict

from kedro.pipeline import Pipeline

# Asegúrate que la siguiente línea es correcta
from rentaptomonttkedro.pipelines import data_engineering as de


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    data_engineering_pipeline = de.create_pipeline()

    return {
        "__default__": data_engineering_pipeline,
        "de": data_engineering_pipeline,
    }

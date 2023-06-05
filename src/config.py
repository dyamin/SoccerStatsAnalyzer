from pathlib import Path
import os


def get_project_root() -> Path:
    return Path(__file__).parent


# database path
# TODO- read data directly from Kaggle using Kaggle API, and save it to the database
database_path = os.path.join(get_project_root(), "../resources", "database.sqlite")

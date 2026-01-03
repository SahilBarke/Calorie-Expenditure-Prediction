# settings.py
from typing import List

DATA_DIR = "../data"
RAW_DATA_FILE = f"{DATA_DIR}/Calorie_expenditure.csv"

def get_feature_columns() -> List[str]:
    """Return the list of feature column names used for modeling."""
    return [
        "Age",
        "Height",
        "Weight",
        "Duration",
        "Heart_Rate",
        "Body_Temp",
        "BMI",
        "BMI_Category"
    ]

def get_target_column() -> str:
    """Return the name of the target column."""
    return "Calories"

RANDOM_SEED = 42

TEST_SIZE = 0.2  # Proportion of data to be used for testing

VALIDATION_SIZE = 0.25  # Proportion of training data to be used for validation
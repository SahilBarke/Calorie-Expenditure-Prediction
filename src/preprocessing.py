import pandas as pd

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform basic data preprocessing steps that are always required.

    Steps:
    - Drop unnecessary columns
    """
    df = df.copy()

    # Drop column that is not useful for modeling
    df = df.drop(columns=["id"])

    return df
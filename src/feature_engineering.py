# src/feature_engineering.py
import pandas as pd

# --------------------------
# Top-level functions
# --------------------------


def calculate_bmi(weight, height):
    """Calculate BMI from weight (kg) and height (cm)"""
    return (weight / ((height / 100) ** 2)).round(2)


def bmi_category(bmi):
    """Return BMI category from BMI value"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


# --------------------------
# Main feature engineering function
# --------------------------
def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform feature engineering on the DataFrame.
    - Adds BMI and BMI category
    """
    df = df.copy()

    # Add BMI column
    df["BMI"] = calculate_bmi(df["Weight"], df["Height"])

    # Add BMI category column
    df["BMI_Category"] = df["BMI"].apply(bmi_category)

    return df

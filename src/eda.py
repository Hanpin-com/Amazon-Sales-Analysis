from __future__ import annotations

import pandas as pd
from config import DATA_PATH


def load_data() -> pd.DataFrame:
    """
    Load the Amazon.csv dataset using a stable absolute path
    derived from the project root (via config.py).
    """
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"CSV not found at: {DATA_PATH}")
    return pd.read_csv(DATA_PATH)


def run_basic_eda() -> None:
    """
    Basic EDA summary for quick sanity checks (RBC-friendly: data quality first).
    """
    df = load_data()

    print("\n--- BASIC EDA ---")
    print("Shape:", df.shape)

    print("\nColumns:", list(df.columns))

    print("\nMissing values (top 10):")
    print(df.isna().sum().sort_values(ascending=False).head(10))

    print("\nDescribe (numeric):")
    # include all numeric columns that exist
    print(df.describe())

    print("\nSample rows:")
    print(df.head())

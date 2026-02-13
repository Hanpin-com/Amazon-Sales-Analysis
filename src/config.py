from pathlib import Path

# Project root = folder that contains "data/" and "amazon.db"
PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = PROJECT_ROOT / "data" / "Amazon.csv"
DB_PATH = PROJECT_ROOT / "amazon.db"

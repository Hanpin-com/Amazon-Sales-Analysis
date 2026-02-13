import sqlite3
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = PROJECT_ROOT / "amazon.db"


def _connect():
    return sqlite3.connect(DB_PATH)


def revenue_by_category():
    conn = _connect()

    query = """
    SELECT
        Category,
        SUM(TotalAmount) AS total_revenue
    FROM sales
    GROUP BY Category
    ORDER BY total_revenue DESC;
    """

    df = pd.read_sql(query, conn)
    conn.close()
    return df


def top_products_by_revenue(limit=10):
    conn = _connect()

    query = f"""
    SELECT
        ProductName,
        SUM(TotalAmount) AS total_revenue
    FROM sales
    GROUP BY ProductName
    ORDER BY total_revenue DESC
    LIMIT {limit};
    """

    df = pd.read_sql(query, conn)
    conn.close()
    return df

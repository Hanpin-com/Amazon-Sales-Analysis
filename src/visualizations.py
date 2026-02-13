from __future__ import annotations

import pandas as pd
import matplotlib.pyplot as plt
from config import DATA_PATH


def load_data() -> pd.DataFrame:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"CSV not found at: {DATA_PATH}")
    return pd.read_csv(DATA_PATH)


def plot_top_products(top_n: int = 10) -> None:
    """
    Top N products by total revenue (TotalAmount).
    Uses: ProductName, TotalAmount
    """
    df = load_data()
    top = (
        df.groupby("ProductName")["TotalAmount"]
          .sum()
          .sort_values(ascending=False)
          .head(top_n)
    )

    plt.figure()
    top.sort_values().plot(kind="barh")  # horizontal for readability
    plt.title(f"Top {top_n} Products by Revenue")
    plt.xlabel("Total Revenue")
    plt.ylabel("Product")
    plt.tight_layout()
    plt.show()


def plot_payment_method_distribution() -> None:
    """
    Count distribution of payment methods.
    Uses: PaymentMethod
    """
    df = load_data()
    dist = df["PaymentMethod"].value_counts()

    plt.figure()
    dist.plot(kind="bar")
    plt.title("Payment Method Distribution (Count)")
    plt.xlabel("Payment Method")
    plt.ylabel("Number of Orders")
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap() -> None:
    """
    Correlation heatmap for numeric columns.
    Uses: numeric columns in dataset (Quantity, UnitPrice, Discount, Tax, ShippingCost, TotalAmount)
    """
    df = load_data()

    numeric_cols = df.select_dtypes(include="number")
    corr = numeric_cols.corr(numeric_only=True)

    plt.figure()
    plt.imshow(corr, aspect="auto")
    plt.title("Correlation Heatmap (Numeric Columns)")
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=45, ha="right")
    plt.yticks(range(len(corr.index)), corr.index)
    plt.colorbar()
    plt.tight_layout()
    plt.show()


def plot_brand_revenue(top_n: int = 10) -> None:
    """
    Top N brands by total revenue.
    Uses: Brand, TotalAmount
    """
    df = load_data()
    top = (
        df.groupby("Brand")["TotalAmount"]
          .sum()
          .sort_values(ascending=False)
          .head(top_n)
    )

    plt.figure()
    top.plot(kind="bar")
    plt.title(f"Top {top_n} Brands by Revenue")
    plt.xlabel("Brand")
    plt.ylabel("Total Revenue")
    plt.tight_layout()
    plt.show()

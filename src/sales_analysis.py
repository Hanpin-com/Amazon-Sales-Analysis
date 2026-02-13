import pandas as pd
import matplotlib.pyplot as plt
from config import DATA_PATH


def load_data() -> pd.DataFrame:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"CSV not found at: {DATA_PATH}")
    df = pd.read_csv(DATA_PATH)
    df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
    return df


def plot_daily_sales() -> None:
    df = load_data()
    daily = (
        df.dropna(subset=["OrderDate"])
          .groupby(df["OrderDate"].dt.date)["TotalAmount"]
          .sum()
          .sort_index()
    )

    plt.figure()
    daily.plot()
    plt.title("Daily Revenue Trend")
    plt.xlabel("Date")
    plt.ylabel("Total Revenue")
    plt.tight_layout()
    plt.show()


def plot_monthly_sales() -> None:
    df = load_data()
    monthly = (
        df.dropna(subset=["OrderDate"])
          .groupby(df["OrderDate"].dt.to_period("M"))["TotalAmount"]
          .sum()
          .sort_index()
    )
    # Convert PeriodIndex to timestamp for plotting
    monthly.index = monthly.index.to_timestamp()

    plt.figure()
    monthly.plot()
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Revenue")
    plt.tight_layout()
    plt.show()


def plot_revenue_by_country(top_n: int = 10) -> None:
    df = load_data()
    by_country = (
        df.groupby("Country")["TotalAmount"]
          .sum()
          .sort_values(ascending=False)
          .head(top_n)
    )

    plt.figure()
    by_country.plot(kind="bar")
    plt.title(f"Top {top_n} Countries by Revenue")
    plt.xlabel("Country")
    plt.ylabel("Total Revenue")
    plt.tight_layout()
    plt.show()


def plot_revenue_by_category(top_n: int = 10) -> None:
    df = load_data()
    by_cat = (
        df.groupby("Category")["TotalAmount"]
          .sum()
          .sort_values(ascending=False)
          .head(top_n)
    )

    plt.figure()
    by_cat.plot(kind="bar")
    plt.title(f"Top {top_n} Categories by Revenue")
    plt.xlabel("Category")
    plt.ylabel("Total Revenue")
    plt.tight_layout()
    plt.show()


def plot_revenue_by_order_status() -> None:
    df = load_data()
    by_status = (
        df.groupby("OrderStatus")["TotalAmount"]
          .sum()
          .sort_values(ascending=False)
    )

    plt.figure()
    by_status.plot(kind="bar")
    plt.title("Revenue by Order Status")
    plt.xlabel("Order Status")
    plt.ylabel("Total Revenue")
    plt.tight_layout()
    plt.show()

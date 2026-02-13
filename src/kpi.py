import sqlite3
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = PROJECT_ROOT / "amazon.db"


def _connect():
    return sqlite3.connect(DB_PATH)


def get_kpi_snapshot():
    conn = _connect()

    # ---------------- Core KPIs ----------------
    core_query = """
    SELECT
        SUM(TotalAmount) AS total_revenue,
        COUNT(*)         AS total_orders,
        AVG(TotalAmount) AS avg_order_value
    FROM sales;
    """
    core = pd.read_sql(core_query, conn)

    total_revenue = core.loc[0, "total_revenue"] or 0
    total_orders = core.loc[0, "total_orders"] or 0
    avg_order_value = core.loc[0, "avg_order_value"] or 0

    # ---------------- Monthly Growth ----------------
    growth_query = """
    SELECT
        strftime('%Y-%m', OrderDate) AS month,
        SUM(TotalAmount) AS revenue
    FROM sales
    GROUP BY month
    ORDER BY month;
    """
    monthly = pd.read_sql(growth_query, conn)

    monthly["growth"] = monthly["revenue"].pct_change()
    latest_growth = monthly["growth"].iloc[-1] if len(monthly) > 1 else 0

    # ---------------- Revenue Concentration (Top 20%) ----------------
    concentration_query = """
    SELECT
        ProductName,
        SUM(TotalAmount) AS revenue
    FROM sales
    GROUP BY ProductName
    ORDER BY revenue DESC;
    """
    products = pd.read_sql(concentration_query, conn)

    top_20_count = int(len(products) * 0.2)
    top_20_revenue = products.head(top_20_count)["revenue"].sum()
    concentration_ratio = top_20_revenue / total_revenue if total_revenue else 0

    # ---------------- Top Category Share ----------------
    category_query = """
    SELECT
        Category,
        SUM(TotalAmount) AS revenue
    FROM sales
    GROUP BY Category
    ORDER BY revenue DESC;
    """
    categories = pd.read_sql(category_query, conn)

    top_category_share = (
        categories.iloc[0]["revenue"] / total_revenue
        if total_revenue else 0
    )

    # ---------------- Repeat Customer Rate ----------------
    repeat_query = """
    SELECT
        CustomerID,
        COUNT(*) AS order_count
    FROM sales
    GROUP BY CustomerID;
    """
    customers = pd.read_sql(repeat_query, conn)

    repeat_customers = customers[customers["order_count"] > 1]
    repeat_rate = len(repeat_customers) / len(customers) if len(customers) else 0

    conn.close()

    return {
        "Total Revenue": total_revenue,
        "Total Orders": total_orders,
        "Avg Order Value": avg_order_value,
        "Latest Monthly Growth %": latest_growth,
        "Revenue Concentration (Top 20%)": concentration_ratio,
        "Top Category Share %": top_category_share,
        "Repeat Customer Rate %": repeat_rate,
    }


def print_kpi_dashboard():
    kpis = get_kpi_snapshot()

    print("\n==========================")
    print("📌 KPI DASHBOARD (Business Intelligence Edition))")
    print("==========================")

    print(f"Total Revenue:                     {kpis['Total Revenue']:,.2f}")
    print(f"Total Orders:                      {kpis['Total Orders']:,}")
    print(f"Average Order Value:               {kpis['Avg Order Value']:,.2f}")

    print(f"Latest Monthly Growth:             {kpis['Latest Monthly Growth %']*100:,.2f}%")
    print(f"Revenue Concentration (Top 20%):   {kpis['Revenue Concentration (Top 20%)']*100:,.2f}%")
    print(f"Top Category Share:                {kpis['Top Category Share %']*100:,.2f}%")
    print(f"Repeat Customer Rate:              {kpis['Repeat Customer Rate %']*100:,.2f}%")

    print("==========================\n")

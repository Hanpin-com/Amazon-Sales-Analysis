from eda import run_basic_eda
from sales_analysis import (
    plot_daily_sales,
    plot_monthly_sales,
    plot_revenue_by_country,
    plot_revenue_by_category,
    plot_revenue_by_order_status,
)
from visualizations import (
    plot_top_products,
    plot_payment_method_distribution,
    plot_correlation_heatmap,
    plot_brand_revenue,
)

# ✅ 新增：KPI Dashboard
from kpi import print_kpi_dashboard


def run_all_analyses() -> None:
    print("\n==========================")
    print("🚀 Starting Amazon Sales Analysis")
    print("==========================\n")

    # ✅ KPI (SQL) first (RBC-friendly)
    print_kpi_dashboard()

    # ------------------ EDA ------------------
    print("🔍 [EDA] Running Basic EDA ...")
    run_basic_eda()
    print("✅ [EDA] Completed Basic EDA\n")

    # ------------------ SALES ANALYSIS ------------------
    print("📈 [Sales] Plotting Daily Sales Trend ...")
    plot_daily_sales()
    print("✅ Daily Sales Trend Completed\n")

    print("📊 [Sales] Plotting Monthly Revenue ...")
    plot_monthly_sales()
    print("✅ Monthly Revenue Completed\n")

    print("🌎 [Sales] Plotting Revenue by Country ...")
    plot_revenue_by_country()
    print("✅ Revenue by Country Completed\n")

    print("🛒 [Sales] Plotting Revenue by Product Category ...")
    plot_revenue_by_category()
    print("✅ Revenue by Product Category Completed\n")

    print("📦 [Sales] Plotting Revenue by Order Status ...")
    plot_revenue_by_order_status()
    print("✅ Revenue by Order Status Completed\n")

    # ------------------ VISUALIZATIONS ------------------
    print("🏆 [Viz] Plotting Top Products (Top 10) ...")
    plot_top_products(top_n=10)
    print("✅ Top Products Completed\n")

    print("💳 [Viz] Plotting Payment Method Distribution ...")
    plot_payment_method_distribution()
    print("✅ Payment Method Distribution Completed\n")

    print("🔥 [Viz] Plotting Correlation Heatmap ...")
    plot_correlation_heatmap()
    print("✅ Correlation Heatmap Completed\n")

    print("🏷️ [Viz] Plotting Top Brands ...")
    plot_brand_revenue(top_n=10)
    print("✅ Top Brands Completed\n")

    print("==========================")
    print("🎉 ALL ANALYSES COMPLETED SUCCESSFULLY!")
    print("==========================\n")


if __name__ == "__main__":
    run_all_analyses()

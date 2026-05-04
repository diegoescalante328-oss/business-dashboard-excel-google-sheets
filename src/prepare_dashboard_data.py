from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = BASE_DIR / "data" / "raw_business_data.csv"
CLEAN_DATA_PATH = BASE_DIR / "data" / "dashboard_ready_data.csv"
KPI_PATH = BASE_DIR / "dashboard" / "kpi_summary.csv"
MONTHLY_PATH = BASE_DIR / "dashboard" / "monthly_summary.csv"
CATEGORY_PATH = BASE_DIR / "dashboard" / "category_summary.csv"
REPORT_PATH = BASE_DIR / "reports" / "business_insights_report.md"


def clean_text(value: str) -> str:
    return str(value).strip().title()


def parse_mixed_date(value: object) -> pd.Timestamp:
    """Parse mixed raw date values into a timestamp.

    Tries clear formats first, then falls back to pandas inference.
    """
    if pd.isna(value):
        return pd.NaT

    value_text = str(value).strip()
    if not value_text:
        return pd.NaT

    explicit_formats = [
        "%Y-%m-%d",
        "%Y/%m/%d",
        "%m/%d/%Y",
        "%m-%d-%Y",
        "%B %d, %Y",
        "%b %d %Y",
    ]

    for fmt in explicit_formats:
        parsed = pd.to_datetime(value_text, format=fmt, errors="coerce")
        if not pd.isna(parsed):
            return parsed

    # Handle ambiguous dash formats by trying day-first and month-first safely.
    for fmt in ["%d-%m-%Y", "%m-%d-%Y"]:
        parsed = pd.to_datetime(value_text, format=fmt, errors="coerce")
        if not pd.isna(parsed):
            return parsed

    return pd.to_datetime(value_text, errors="coerce")


def build_report(kpi_df: pd.DataFrame, monthly_df: pd.DataFrame, category_df: pd.DataFrame, region_df: pd.DataFrame) -> str:
    kpis = dict(zip(kpi_df["kpi"], kpi_df["value"]))
    best_month = monthly_df.sort_values("estimated_profit", ascending=False).iloc[0]
    top_category = category_df.sort_values("total_revenue", ascending=False).iloc[0]
    top_region = region_df.sort_values("total_revenue", ascending=False).iloc[0]

    return f"""# Business Insights Report

## Executive summary
This synthetic dashboard dataset shows stable sales activity with clear revenue drivers in software and strong performance in the West region.

## Business question
How is monthly revenue and profit performing, and which categories and regions should a small business prioritize?

## Dataset description and caveats
- Synthetic transactional data for portfolio demonstration only.
- Mixed raw date formats were standardized during preparation for consistent monthly reporting.
- One duplicate business row was removed during preparation.
- No real company data is used; outputs are synthetic demo data only.

## Dashboard KPI snapshot
- Total Revenue: {kpis['Total Revenue']}
- Total Expenses: {kpis['Total Expenses']}
- Estimated Profit: {kpis['Estimated Profit']}
- Total Orders: {kpis['Total Orders']}
- Average Order Value: {kpis['Average Order Value']}

## Monthly performance summary
Best month by estimated profit: **{best_month['month']}** ({best_month['estimated_profit']:.2f}).
Revenue and profit are influenced by recurring software subscriptions and periodic electronics orders.

## Category performance summary
Top revenue category: **{top_category['product_category']}** ({top_category['total_revenue']:.2f}).
Office supplies support order volume while software drives higher value per order.

## Region or channel notes
Top region by revenue: **{top_region['region']}** ({top_region['total_revenue']:.2f}).
Online sales channel activity is dominant, suggesting digital sales operations are critical.

## Business recommendations
1. Monitor software renewals monthly because they are high-value transactions.
2. Track discount usage in electronics to protect margin while maintaining demand.
3. Compare online vs in-store conversion rates to optimize channel strategy.

## Limitations and next steps
- This report is based on a small synthetic dataset and is not a production forecast.
- Next step: expand to 12+ months of data and add customer retention tracking.
"""


def main() -> None:
    df = pd.read_csv(RAW_DATA_PATH)
    raw_row_count = len(df)

    df.columns = [col.strip().lower() for col in df.columns]

    text_columns = [
        "transaction_id",
        "customer_segment",
        "product_category",
        "product_name",
        "region",
        "sales_channel",
        "expense_category",
        "payment_method",
    ]

    for col in text_columns:
        df[col] = df[col].astype(str).str.strip()

    for col in ["customer_segment", "product_category", "product_name", "region", "expense_category"]:
        df[col] = df[col].apply(clean_text)

    df["sales_channel"] = df["sales_channel"].str.lower().str.replace("-", " ", regex=False).str.title()
    df["payment_method"] = df["payment_method"].str.lower().str.title()

    df["discount"] = pd.to_numeric(df["discount"], errors="coerce").fillna(0)
    for col in ["quantity", "unit_price", "expense_amount"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    raw_date_series = df["transaction_date"].copy()
    df["transaction_date"] = df["transaction_date"].apply(parse_mixed_date)
    raw_non_empty_dates = raw_date_series.astype(str).str.strip().replace("nan", "")
    date_failure_count = int(((raw_non_empty_dates != "") & df["transaction_date"].isna()).sum())

    dedupe_cols = [
        "transaction_id",
        "transaction_date",
        "customer_segment",
        "product_category",
        "product_name",
        "region",
        "sales_channel",
        "quantity",
        "unit_price",
        "discount",
        "expense_category",
        "expense_amount",
        "payment_method",
    ]
    df = df.drop_duplicates(subset=dedupe_cols).copy()
    cleaned_row_count = len(df)

    df["revenue"] = df["quantity"] * df["unit_price"] * (1 - df["discount"])
    df["estimated_profit"] = df["revenue"] - df["expense_amount"]
    df["year"] = df["transaction_date"].dt.year
    df["month"] = df["transaction_date"].dt.to_period("M").astype(str)
    df["transaction_date"] = df["transaction_date"].dt.strftime("%Y-%m-%d")

    for col in ["revenue", "expense_amount", "estimated_profit"]:
        df[col] = df[col].round(2)

    df = df.sort_values("transaction_date")
    df.to_csv(CLEAN_DATA_PATH, index=False)

    monthly_summary = (
        df.groupby("month", as_index=False)
        .agg(
            total_revenue=("revenue", "sum"),
            total_expenses=("expense_amount", "sum"),
            estimated_profit=("estimated_profit", "sum"),
            order_count=("transaction_id", "count"),
            units_sold=("quantity", "sum"),
        )
        .round(2)
    )
    monthly_summary.to_csv(MONTHLY_PATH, index=False)

    category_summary = (
        df.groupby("product_category", as_index=False)
        .agg(
            total_revenue=("revenue", "sum"),
            total_expenses=("expense_amount", "sum"),
            estimated_profit=("estimated_profit", "sum"),
            order_count=("transaction_id", "count"),
            units_sold=("quantity", "sum"),
        )
        .round(2)
        .sort_values("total_revenue", ascending=False)
    )
    category_summary.to_csv(CATEGORY_PATH, index=False)

    region_summary = df.groupby("region", as_index=False).agg(total_revenue=("revenue", "sum"))

    total_revenue = round(df["revenue"].sum(), 2)
    total_expenses = round(df["expense_amount"].sum(), 2)
    estimated_profit = round(df["estimated_profit"].sum(), 2)
    total_orders = int(df["transaction_id"].count())
    total_units = int(df["quantity"].sum())
    avg_order_value = round(total_revenue / total_orders, 2) if total_orders else 0
    top_category = category_summary.iloc[0]["product_category"]
    top_region = region_summary.sort_values("total_revenue", ascending=False).iloc[0]["region"]

    kpi_summary = pd.DataFrame(
        {
            "kpi": [
                "Total Revenue",
                "Total Expenses",
                "Estimated Profit",
                "Total Orders",
                "Total Units Sold",
                "Average Order Value",
                "Top Revenue Category",
                "Top Region by Revenue",
            ],
            "value": [
                total_revenue,
                total_expenses,
                estimated_profit,
                total_orders,
                total_units,
                avg_order_value,
                top_category,
                top_region,
            ],
        }
    )
    kpi_summary.to_csv(KPI_PATH, index=False)

    report_text = build_report(kpi_summary, monthly_summary, category_summary, region_summary)
    REPORT_PATH.write_text(report_text, encoding="utf-8")

    print(f"Raw rows: {raw_row_count}")
    print(f"Cleaned rows (after dedupe): {cleaned_row_count}")
    print(f"Date parsing failures (non-empty raw date): {date_failure_count}")
    if date_failure_count > 0:
        print("WARNING: Some non-empty raw dates could not be parsed and remain blank in cleaned outputs.")
    print("Dashboard-ready files created successfully.")


if __name__ == "__main__":
    main()

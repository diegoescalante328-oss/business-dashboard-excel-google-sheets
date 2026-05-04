# Dashboard Overview

## Purpose
This dashboard helps a small business owner review monthly sales performance, costs, and estimated profit using clean, spreadsheet-ready summary tables.

## KPI meanings
- **Total Revenue:** Total sales value after discounts.
- **Total Expenses:** Total recorded expense amounts linked to transactions.
- **Estimated Profit:** Revenue minus expense amount.
- **Total Orders:** Number of cleaned transactions.
- **Total Units Sold:** Sum of quantity sold.
- **Average Order Value:** Revenue divided by number of orders.
- **Top Revenue Category:** Product category with highest revenue.
- **Top Region by Revenue:** Region contributing the highest revenue.

## Summary tables
- `monthly_summary.csv` supports monthly trend analysis for revenue, expenses, and profit.
- `category_summary.csv` supports category-level contribution and margin comparisons.
- `kpi_summary.csv` supports headline KPI cards for a management dashboard.

## Recreate in Excel or Google Sheets
1. Import CSV summary files.
2. Build KPI cards from `kpi_summary.csv`.
3. Use a line chart for monthly revenue and estimated profit trends.
4. Use bar charts for revenue by category and revenue by region.

## What a business owner should review first
1. Total Revenue vs Estimated Profit.
2. Best/worst months in `monthly_summary.csv`.
3. Top category and top region to validate focus areas.

# Business Dashboard Portfolio Scaffold

**Value proposition:** A lightweight, client-friendly workflow that turns messy spreadsheet sales data into dashboard-ready KPI tables and a business insight report.

## Overview
This project demonstrates a practical reporting process often requested by small business clients on Upwork and LinkedIn: clean raw spreadsheet exports, calculate core KPIs, and produce simple monthly/category summaries for dashboarding.

## Business problem
Small businesses often track sales and expenses in spreadsheets but struggle to convert that data into clear performance insights.

## Synthetic data and privacy note
All data in this repository is synthetic and created for portfolio use. No real company, customer, or private data is included.

## Tools used
- Python
- pandas
- CSV + Markdown deliverables
- Excel/Google Sheets compatible outputs

## Workflow
1. Load raw spreadsheet-style transactional data (`data/raw_business_data.csv`).
2. Clean fields (spaces, capitalization, mixed dates, missing discount values, duplicates).
3. Calculate revenue and estimated profit.
4. Produce dashboard-ready data and summary tables.
5. Generate a short client-facing insights report.

## Client deliverables
- Cleaned dashboard dataset
- KPI summary
- Monthly summary
- Category summary
- Business insights report
- Documentation for Excel/Google Sheets dashboard build

## Dashboard outputs
- `dashboard/kpi_summary.csv`
- `dashboard/monthly_summary.csv`
- `dashboard/category_summary.csv`

## Key insights (example)
- Which month had strongest profit.
- Which product category generated the most revenue.
- Which region contributed the highest revenue.

## How to run
```bash
python src/prepare_dashboard_data.py
```

## Repository structure
See folder-level outputs in `data/`, `dashboard/`, `reports/`, and `docs/`.

## Limitations
- Synthetic and small dataset.
- No live integrations or automated refresh.
- No visualization binaries in this first PR.

## Future improvements
- Add 12+ months of synthetic history.
- Add optional Excel/Google Sheets dashboard screenshots in later PRs.
- Add separate regional/channel summaries.

## License
MIT License. See `LICENSE`.

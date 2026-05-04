# Business Dashboard Reporting Portfolio (Excel + Google Sheets)

**Value proposition:** This project shows how messy spreadsheet-style business data can be cleaned into dashboard-ready tables and plain-English reporting notes that a small business owner can review quickly.

## What business problem this solves
Small businesses often have sales and expense exports in CSV or spreadsheet form, but not a clear monthly performance view. This project demonstrates a practical workflow to convert that raw data into usable KPI and summary outputs for reporting.

## What this project produces
- Cleaned, dashboard-ready dataset (`data/dashboard_ready_data.csv`)
- KPI summary table (`dashboard/kpi_summary.csv`)
- Monthly performance table (`dashboard/monthly_summary.csv`)
- Category performance table (`dashboard/category_summary.csv`)
- Plain-English business insights report (`reports/business_insights_report.md`)
- Excel/Google Sheets dashboard build notes (`docs/dashboard_build_notes.md`)

## Synthetic data and privacy
All data in this repository is synthetic (sample data created for portfolio/demo use). No real company data, private data, APIs, secrets, or paid services are used.

## Start Here
### For clients
1. Read **Client Deliverables** below.
2. Review `dashboard/kpi_summary.csv`.
3. Review `reports/business_insights_report.md`.

### For technical reviewers
1. Review `src/prepare_dashboard_data.py`.
2. Compare `data/raw_business_data.csv` and `data/dashboard_ready_data.csv`.
3. Run: `python src/prepare_dashboard_data.py`.

### For spreadsheet/dashboard users
1. Review `docs/dashboard_build_notes.md`.
2. Review `dashboard/monthly_summary.csv`.
3. Review `dashboard/category_summary.csv`.

## Client Deliverables
For a client-style dashboard/reporting engagement, this project structure can produce:
- Cleaned dashboard-ready dataset
- KPI summary table
- Monthly performance table
- Category performance table
- Business insights report
- Excel/Google Sheets dashboard build notes

This repository is a portfolio demonstration using synthetic data and does not claim real business ROI.

## Skills Demonstrated
- Spreadsheet data cleanup for inconsistent exports
- KPI definition for business reporting
- Dashboard-ready summary table generation
- Monthly trend reporting structure
- Category performance reporting structure
- Business insight communication in plain English
- Reproducible Python workflow (`python src/prepare_dashboard_data.py`)
- Excel/Google Sheets dashboard planning

## How to run
```bash
python src/prepare_dashboard_data.py
```

## Repository Structure
```text
business-dashboard-excel-google-sheets/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── src/
│   └── prepare_dashboard_data.py
├── data/
│   ├── raw_business_data.csv
│   └── dashboard_ready_data.csv
├── dashboard/
│   ├── kpi_summary.csv
│   ├── monthly_summary.csv
│   ├── category_summary.csv
│   └── dashboard_overview.md
├── reports/
│   └── business_insights_report.md
├── docs/
│   ├── client_delivery_notes.md
│   ├── dashboard_build_notes.md
│   └── data_dictionary.md
└── visuals/
    └── .gitkeep
```

## License
MIT License. See `LICENSE`.

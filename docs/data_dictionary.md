# Data Dictionary

| Column Name | Description | Data Type | Source/Status | Notes |
|---|---|---|---|---|
| transaction_id | Unique transaction reference | text | raw/cleaned | Used as order identifier |
| transaction_date | Date of transaction | date | raw/cleaned | Mixed formats parsed to standard date |
| customer_segment | Customer type segment | text | raw/cleaned | Standardized capitalization |
| product_category | Product grouping | text | raw/cleaned | Used for category summary |
| product_name | Product label | text | raw/cleaned | Trimmed spaces |
| region | Sales region | text | raw/cleaned | Standardized capitalization |
| sales_channel | Where sale happened | text | raw/cleaned | Online/In Store standardized |
| quantity | Units sold in transaction | number | raw/cleaned | Converted to numeric |
| unit_price | Price per unit | number | raw/cleaned | Converted to numeric |
| discount | Discount rate (0-1) | number | raw/cleaned | Missing values filled with 0 |
| expense_category | Expense type label | text | raw/cleaned | Trimmed and title-cased |
| expense_amount | Expense amount linked to transaction | number | raw/cleaned | Converted to numeric |
| payment_method | Payment type | text | raw/cleaned | Standardized capitalization |
| revenue | quantity * unit_price * (1-discount) | number | calculated | Main sales KPI metric |
| estimated_profit | revenue - expense_amount | number | calculated | Simplified margin estimate |
| year | Year extracted from transaction_date | integer | calculated | For filtering/grouping |
| month | Year-month period (YYYY-MM) | text | calculated | Used for monthly summaries |

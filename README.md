# Retail Intelligence Platform

End-to-end retail analytics platform built with Python, Pandas, SQL, SQLite and Power BI.

The project includes ETL pipelines, data cleaning & validation, analytical SQL views and an interactive BI dashboard for revenue, profitability and customer behavior analysis.

---

## Dashboard Preview

![Dashboard Preview](images/dashboard.jpg)

---

## Features

- Automated ETL pipeline
- Synthetic retail data generation
- Data cleaning and validation
- SQLite database integration
- Analytical SQL views
- KPI monitoring
- Revenue trend analysis
- Customer segmentation
- Category profitability analysis
- Return rate analytics
- Interactive Power BI dashboard
- Executive business insights panel
- Dynamic filtering system

---

## Tech Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Processing | Pandas |
| Database | SQLite |
| Analytics | SQL |
| BI & Visualization | Power BI |
| Version Control | Git & GitHub |

---

## Project Structure

```text
retail-intelligence-platform/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── images/
│   └── dashboard.jpg
│
├── powerbi/
│   └── retail_dashboard.pbix
│
├── sql/
│   ├── create_tables.sql
│   ├── create_views.sql
│   ├── kpi_queries.sql
│   ├── cohort_retention.sql
│   └── rfm_analysis.sql
│
├── src/
│   ├── cleaner.py
│   ├── create_views.py
│   ├── data_generator.py
│   ├── database.py
│   └── validator.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Dashboard Overview

The Power BI dashboard provides:

- Revenue KPI monitoring
- Monthly revenue trend analysis
- Customer segmentation analytics
- Category profitability analysis
- Return rate monitoring
- Interactive filtering system
- Executive business insights

---

## Data Pipeline

The analytics pipeline includes:

1. Synthetic retail data generation
2. Data cleaning with Pandas
3. Data validation
4. SQLite database loading
5. SQL analytics view creation
6. Power BI dashboard visualization

---

## Example Analytics

The platform supports analytics such as:

- Revenue trends
- Average order value (AOV)
- Return rate analysis
- Customer segmentation
- Gross margin analysis
- Category performance
- Cohort retention analysis
- RFM analysis

---

## Run Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the full pipeline:

```bash
python main.py --all
```

This will:

1. Generate synthetic retail data
2. Validate raw data
3. Clean data
4. Load processed data into SQLite
5. Create SQL analytics views

---

## Power BI Dashboard

The Power BI dashboard includes:

- KPI cards
- Revenue trend monitoring
- Customer segmentation visuals
- Category profitability analysis
- Return rate tracking
- Interactive slicers
- Executive insights section

Dashboard file:

```text
powerbi/retail_dashboard.pbix
```

---

## Future Improvements

- Advanced DAX measures
- Automated dashboard refresh
- Real-time analytics
- Docker containerization
- PostgreSQL integration
- CI/CD automation
- Cloud deployment

---

## Author

Ruslan Tuliei

GitHub: https://github.com/offANTI
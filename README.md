# Retail Intelligence Platform

End-to-end retail analytics platform built with Python, Pandas, SQL, SQLite and Power BI.  
The project includes ETL pipelines, data cleaning & validation, analytical SQL views and an interactive BI dashboard for revenue, profitability and customer behavior analysis.

---

## Dashboard Preview

![Dashboard Preview](images/dashboard.jpg)

---

## Features

- Automated ETL pipeline
- Retail data generation
- Data cleaning and validation
- SQLite database integration
- Analytical SQL views
- KPI monitoring
- Revenue trend analysis
- Customer segmentation
- Category profitability analysis
- Return rate analytics
- Interactive Power BI dashboard
- Business insights panel
- Dynamic filtering system

---

## Tech Stack

- Python
- Pandas
- SQL
- SQLite
- Power BI
- Git & GitHub

---

## Project Structure

```text
retail-intelligence-platform/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── images/
│   └── dashboard.jpg
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
├── retail_intelligence.db
└── README.md
```

---

## Dashboard Overview

The Power BI dashboard provides:

- Revenue KPI tracking
- Monthly revenue trend monitoring
- Customer segment analysis
- Category profitability analysis
- Return rate monitoring
- Interactive filtering
- Executive business insights

---

## Data Pipeline

The project pipeline includes:

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
- Average order value
- Return rate analysis
- Customer segmentation
- Gross margin analysis
- Category performance
- Cohort and retention analysis
- RFM analysis

---

## Run Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the pipeline:

```bash
python main.py
```

Create SQL analytics views:

```bash
python src/create_views.py
```

---

## Power BI Dashboard

The dashboard was built using:

- SQL analytical views
- Interactive slicers
- KPI cards
- Business insights section
- Revenue and profitability charts

---

## Future Improvements

- Advanced DAX measures
- Real-time data refresh
- Cloud deployment
- Automated reporting
- Docker containerization
- PostgreSQL integration
- CI/CD automation

---
## Power BI Dashboard

The interactive Power BI dashboard file is available in:

```text
powerbi/retail_dashboard.pbix
```
---
## Author

Ruslan Tuliei

GitHub: https://github.com/offANTI

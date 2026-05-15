import logging
import sqlite3
from pathlib import Path

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)

PROCESSED_DATA_DIR = Path("data/processed")
DB_PATH = Path("retail_intelligence.db")


def load_csv_to_sqlite(file_name: str, table_name: str) -> None:
    file_path = PROCESSED_DATA_DIR / file_name

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(file_path)

    with sqlite3.connect(DB_PATH) as conn:
        df.to_sql(table_name, conn, if_exists="replace", index=False)

    logger.info("Loaded %s rows into table '%s'.", len(df), table_name)


def load_all_raw_data() -> None:
    logger.info("Loading raw CSV files into SQLite database.")

    tables = {
        "customers.csv": "customers",
        "products.csv": "products",
        "orders.csv": "orders",
        "order_items.csv": "order_items",
        "returns.csv": "returns",
    }

    for file_name, table_name in tables.items():
        load_csv_to_sqlite(file_name, table_name)

    logger.info("All raw data loaded successfully into %s.", DB_PATH)


if __name__ == "__main__":
    load_all_raw_data()
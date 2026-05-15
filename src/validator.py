import logging
from pathlib import Path

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)

RAW_DATA_DIR = Path("data/raw")

REQUIRED_COLUMNS = {
    "customers": {
        "customer_id",
        "customer_name",
        "city",
        "country",
        "signup_date",
        "customer_segment",
    },
    "products": {
        "product_id",
        "product_name",
        "category",
        "brand",
        "cost_price",
        "sale_price",
    },
    "orders": {
        "order_id",
        "customer_id",
        "order_date",
        "store_region",
        "payment_method",
    },
    "order_items": {
        "order_item_id",
        "order_id",
        "product_id",
        "quantity",
        "unit_price",
        "discount",
    },
    "returns": {
        "return_id",
        "order_item_id",
        "return_date",
        "return_reason",
    },
}


def validate_required_files() -> None:
    for table_name in REQUIRED_COLUMNS:
        file_path = RAW_DATA_DIR / f"{table_name}.csv"

        if not file_path.exists():
            raise FileNotFoundError(f"Missing required raw file: {file_path}")

    logger.info("All required raw files exist.")


def validate_required_columns(table_name: str, df: pd.DataFrame) -> None:
    required_columns = REQUIRED_COLUMNS[table_name]
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing columns in {table_name}: {missing_columns}"
        )


def validate_not_empty(table_name: str, df: pd.DataFrame) -> None:
    if df.empty:
        raise ValueError(f"{table_name} is empty.")


def validate_numeric_rules(table_name: str, df: pd.DataFrame) -> None:
    if table_name == "products":
        if (df["cost_price"] < 0).any():
            raise ValueError("products.cost_price contains negative values.")

        if (df["sale_price"] < 0).any():
            raise ValueError("products.sale_price contains negative values.")

    if table_name == "order_items":
        if (df["quantity"] <= 0).any():
            raise ValueError("order_items.quantity contains invalid values.")

        if (df["unit_price"] < 0).any():
            raise ValueError("order_items.unit_price contains negative values.")

        if ((df["discount"] < 0) | (df["discount"] > 1)).any():
            raise ValueError("order_items.discount must be between 0 and 1.")


def validate_raw_data() -> None:
    logger.info("Starting raw data validation.")

    validate_required_files()

    for table_name in REQUIRED_COLUMNS:
        file_path = RAW_DATA_DIR / f"{table_name}.csv"
        df = pd.read_csv(file_path)

        validate_not_empty(table_name, df)
        validate_required_columns(table_name, df)
        validate_numeric_rules(table_name, df)

        logger.info("Validated %s: %s rows.", table_name, len(df))

    logger.info("Raw data validation completed successfully.")


if __name__ == "__main__":
    validate_raw_data()
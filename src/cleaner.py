import logging
from pathlib import Path

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)

RAW_DATA_DIR = Path("data/raw")
PROCESSED_DATA_DIR = Path("data/processed")


def clean_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()

    text_columns = data.select_dtypes(include=["object", "string"]).columns

    for column in text_columns:
        data[column] = data[column].astype(str).str.strip()

    return data


def clean_customers(df: pd.DataFrame) -> pd.DataFrame:
    data = clean_text_columns(df)
    data["signup_date"] = pd.to_datetime(data["signup_date"], errors="raise")
    data = data.drop_duplicates(subset=["customer_id"])

    return data


def clean_products(df: pd.DataFrame) -> pd.DataFrame:
    data = clean_text_columns(df)

    data["cost_price"] = pd.to_numeric(data["cost_price"], errors="raise")
    data["sale_price"] = pd.to_numeric(data["sale_price"], errors="raise")

    data = data.drop_duplicates(subset=["product_id"])

    return data


def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    data = clean_text_columns(df)

    data["order_date"] = pd.to_datetime(data["order_date"], errors="raise")
    data = data.drop_duplicates(subset=["order_id"])

    return data


def clean_order_items(df: pd.DataFrame) -> pd.DataFrame:
    data = clean_text_columns(df)

    data["quantity"] = pd.to_numeric(data["quantity"], errors="raise")
    data["unit_price"] = pd.to_numeric(data["unit_price"], errors="raise")
    data["discount"] = pd.to_numeric(data["discount"], errors="raise")

    data = data.drop_duplicates(subset=["order_item_id"])

    return data


def clean_returns(df: pd.DataFrame) -> pd.DataFrame:
    data = clean_text_columns(df)

    data["return_date"] = pd.to_datetime(data["return_date"], errors="raise")
    data = data.drop_duplicates(subset=["return_id"])

    return data


def save_cleaned_data(table_name: str, df: pd.DataFrame) -> None:
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    output_path = PROCESSED_DATA_DIR / f"{table_name}.csv"
    df.to_csv(output_path, index=False)

    logger.info("Saved cleaned %s: %s rows.", table_name, len(df))


def clean_all_raw_data() -> None:
    logger.info("Starting raw data cleaning.")

    cleaning_functions = {
        "customers": clean_customers,
        "products": clean_products,
        "orders": clean_orders,
        "order_items": clean_order_items,
        "returns": clean_returns,
    }

    for table_name, cleaning_function in cleaning_functions.items():
        input_path = RAW_DATA_DIR / f"{table_name}.csv"

        if not input_path.exists():
            raise FileNotFoundError(f"Missing raw file: {input_path}")

        raw_df = pd.read_csv(input_path)
        cleaned_df = cleaning_function(raw_df)

        save_cleaned_data(table_name, cleaned_df)

    logger.info("Raw data cleaning completed successfully.")


if __name__ == "__main__":
    clean_all_raw_data()
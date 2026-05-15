import logging
from pathlib import Path
import random

import numpy as np
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)

RAW_DATA_DIR = Path("data/raw")
RANDOM_SEED = 42

N_CUSTOMERS = 1_000
N_PRODUCTS = 120
N_ORDERS = 10_000

COUNTRIES = ["Germany"]
CITIES = ["Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt", "Dresden"]
REGIONS = ["North", "South", "West", "East", "Central"]
PAYMENT_METHODS = ["Credit Card", "PayPal", "Invoice", "Bank Transfer"]
CUSTOMER_SEGMENTS = ["Consumer", "Business", "Premium"]

CATEGORIES = {
    "Electronics": ["TechPro", "NovaTech", "ElectroMax"],
    "Home": ["HomePlus", "CasaLux", "LivingArt"],
    "Fashion": ["UrbanStyle", "ModeWerk", "StreetLine"],
    "Sports": ["FitZone", "ActivePro", "Sportiva"],
    "Beauty": ["PureCare", "GlowUp", "SkinLab"],
}

RETURN_REASONS = [
    "Damaged product",
    "Wrong size",
    "Late delivery",
    "Changed mind",
    "Product not as described",
]


def generate_customers() -> pd.DataFrame:
    customers = []

    for customer_id in range(1, N_CUSTOMERS + 1):
        customers.append(
            {
                "customer_id": customer_id,
                "customer_name": f"Customer_{customer_id}",
                "city": random.choice(CITIES),
                "country": random.choice(COUNTRIES),
                "signup_date": pd.Timestamp("2022-01-01")
                + pd.to_timedelta(random.randint(0, 900), unit="D"),
                "customer_segment": random.choice(CUSTOMER_SEGMENTS),
            }
        )

    return pd.DataFrame(customers)


def generate_products() -> pd.DataFrame:
    products = []

    for product_id in range(1, N_PRODUCTS + 1):
        category = random.choice(list(CATEGORIES.keys()))
        brand = random.choice(CATEGORIES[category])
        cost_price = round(random.uniform(5, 500), 2)
        markup = random.uniform(1.2, 2.5)
        sale_price = round(cost_price * markup, 2)

        products.append(
            {
                "product_id": product_id,
                "product_name": f"{brand}_{category}_{product_id}",
                "category": category,
                "brand": brand,
                "cost_price": cost_price,
                "sale_price": sale_price,
            }
        )

    return pd.DataFrame(products)


def generate_orders(customers: pd.DataFrame) -> pd.DataFrame:
    orders = []

    customer_ids = customers["customer_id"].tolist()

    for order_id in range(1, N_ORDERS + 1):
        orders.append(
            {
                "order_id": order_id,
                "customer_id": random.choice(customer_ids),
                "order_date": pd.Timestamp("2023-01-01")
                + pd.to_timedelta(random.randint(0, 730), unit="D"),
                "store_region": random.choice(REGIONS),
                "payment_method": random.choice(PAYMENT_METHODS),
            }
        )

    return pd.DataFrame(orders)


def generate_order_items(
    orders: pd.DataFrame,
    products: pd.DataFrame,
) -> pd.DataFrame:
    order_items = []
    order_item_id = 1

    product_ids = products["product_id"].tolist()
    product_price_map = products.set_index("product_id")["sale_price"].to_dict()

    for order_id in orders["order_id"]:
        number_of_items = random.randint(1, 4)

        selected_products = random.sample(product_ids, number_of_items)

        for product_id in selected_products:
            quantity = random.randint(1, 5)
            discount = random.choice([0, 0, 0, 0.05, 0.10, 0.15])
            unit_price = product_price_map[product_id]

            order_items.append(
                {
                    "order_item_id": order_item_id,
                    "order_id": order_id,
                    "product_id": product_id,
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "discount": discount,
                }
            )

            order_item_id += 1

    return pd.DataFrame(order_items)


def generate_returns(order_items: pd.DataFrame) -> pd.DataFrame:
    returned_items = order_items.sample(frac=0.08, random_state=RANDOM_SEED)

    returns = []

    for return_id, row in enumerate(returned_items.itertuples(), start=1):
        returns.append(
            {
                "return_id": return_id,
                "order_item_id": row.order_item_id,
                "return_date": pd.Timestamp("2023-01-01")
                + pd.to_timedelta(random.randint(0, 760), unit="D"),
                "return_reason": random.choice(RETURN_REASONS),
            }
        )

    return pd.DataFrame(returns)


def save_raw_data(dataframes: dict[str, pd.DataFrame]) -> None:
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    for name, dataframe in dataframes.items():
        output_path = RAW_DATA_DIR / f"{name}.csv"
        dataframe.to_csv(output_path, index=False)
        logger.info("Saved %s rows to %s", len(dataframe), output_path)


def generate_retail_data() -> None:
    random.seed(RANDOM_SEED)
    np.random.seed(RANDOM_SEED)

    logger.info("Generating synthetic retail dataset.")

    customers = generate_customers()
    products = generate_products()
    orders = generate_orders(customers)
    order_items = generate_order_items(orders, products)
    returns = generate_returns(order_items)

    save_raw_data(
        {
            "customers": customers,
            "products": products,
            "orders": orders,
            "order_items": order_items,
            "returns": returns,
        }
    )

    logger.info("Synthetic retail dataset generated successfully.")


if __name__ == "__main__":
    generate_retail_data()
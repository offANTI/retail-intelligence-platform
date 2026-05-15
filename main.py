import argparse
import logging
import time

from src.cleaner import clean_all_raw_data
from src.create_views import create_analytics_views
from src.data_generator import generate_retail_data
from src.database import load_all_raw_data
from src.validator import validate_raw_data

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)


def run_pipeline(
    generate_data: bool = False,
    validate_data: bool = False,
    clean_data: bool = False,
    load_data: bool = False,
    create_views: bool = False,
) -> None:

    start_time = time.time()

    logger.info("Starting Retail Intelligence Platform pipeline.")

    if generate_data:
        logger.info("STEP 1: Generating synthetic retail data.")
        generate_retail_data()

    if validate_data:
        logger.info("STEP 2: Validating raw data.")
        validate_raw_data()

    if clean_data:
        logger.info("STEP 3: Cleaning raw data.")
        clean_all_raw_data()

    if load_data:
        logger.info("STEP 4: Loading processed data into SQLite.")
        load_all_raw_data()

    if create_views:
        logger.info("STEP 5: Creating analytics views.")
        create_analytics_views()

    execution_time = round(time.time() - start_time, 2)

    logger.info(
        "Pipeline finished successfully in %s seconds.",
        execution_time,
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Retail Intelligence Platform CLI"
    )

    parser.add_argument(
        "--generate",
        action="store_true",
        help="Generate synthetic retail data.",
    )

    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate raw retail data.",
    )

    parser.add_argument(
        "--clean",
        action="store_true",
        help="Clean raw retail data.",
    )

    parser.add_argument(
        "--load",
        action="store_true",
        help="Load processed data into SQLite.",
    )

    parser.add_argument(
        "--views",
        action="store_true",
        help="Create analytics SQL views.",
    )

    parser.add_argument(
        "--all",
        action="store_true",
        help="Run full retail analytics pipeline.",
    )

    args = parser.parse_args()

    if args.all:
        run_pipeline(
            generate_data=True,
            validate_data=True,
            clean_data=True,
            load_data=True,
            create_views=True,
        )

    else:
        run_pipeline(
            generate_data=args.generate,
            validate_data=args.validate,
            clean_data=args.clean,
            load_data=args.load,
            create_views=args.views,
        )


if __name__ == "__main__":
    main()
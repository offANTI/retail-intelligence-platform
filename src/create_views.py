import logging
import sqlite3
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)

DB_PATH = Path("retail_intelligence.db")
VIEWS_SQL_PATH = Path("sql/create_views.sql")


def create_analytics_views() -> None:
    if not DB_PATH.exists():
        raise FileNotFoundError(f"Database not found: {DB_PATH}")

    if not VIEWS_SQL_PATH.exists():
        raise FileNotFoundError(f"SQL file not found: {VIEWS_SQL_PATH}")

    sql_script = VIEWS_SQL_PATH.read_text(encoding="utf-8")

    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript(sql_script)

    logger.info("Analytics views created successfully.")


if __name__ == "__main__":
    create_analytics_views()
import sqlite3

conn = sqlite3.connect("retail_intelligence.db")

query = """
WITH customer_revenue AS (
    SELECT
        c.customer_id,
        c.customer_segment,
        ROUND(
            SUM(oi.quantity * oi.unit_price * (1 - oi.discount)),
            2
        ) AS revenue
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
    JOIN order_items oi
        ON o.order_id = oi.order_id
    GROUP BY
        c.customer_id,
        c.customer_segment
),
customer_tiers AS (
    SELECT
        customer_id,
        customer_segment,
        revenue,
        CASE
            WHEN revenue > 70000 THEN 'VIP'
            WHEN revenue > 50000 THEN 'Gold'
            ELSE 'Regular'
        END AS customer_tier
    FROM customer_revenue
)
"""

cursor = conn.cursor()
cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

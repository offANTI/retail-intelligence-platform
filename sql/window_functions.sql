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

ranked_customers AS (
    SELECT
        customer_id,
        customer_segment,
        revenue,
        RANK() OVER (
            PARTITION BY customer_segment
            ORDER BY revenue DESC
        ) AS revenue_rank
    FROM customer_revenue
)

SELECT
    customer_id,
    customer_segment,
    revenue,
    revenue_rank
FROM ranked_customers
WHERE revenue_rank <= 3
ORDER BY
    customer_segment,
    revenue_rank;
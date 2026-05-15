WITH customer_metrics AS (

    SELECT
        c.customer_id,
        c.customer_name,
        c.customer_segment,

        MAX(o.order_date) AS last_order_date,

        COUNT(DISTINCT o.order_id) AS total_orders,

        ROUND(
            SUM(
                oi.quantity * oi.unit_price * (1 - oi.discount)
            ),
            2
        ) AS total_revenue

    FROM customers c

    JOIN orders o
        ON c.customer_id = o.customer_id

    JOIN order_items oi
        ON o.order_id = oi.order_id

    GROUP BY
        c.customer_id,
        c.customer_name,
        c.customer_segment
),

rfm_scores AS (

    SELECT
        customer_id,
        customer_name,
        customer_segment,
        last_order_date,
        total_orders,
        total_revenue,

        JULIANDAY('2025-01-01') - JULIANDAY(last_order_date)
            AS recency_days,

        NTILE(5) OVER (
            ORDER BY total_orders DESC
        ) AS frequency_score,

        NTILE(5) OVER (
            ORDER BY total_revenue DESC
        ) AS monetary_score

    FROM customer_metrics
)

SELECT
    customer_id,
    customer_name,
    customer_segment,
    recency_days,
    total_orders,
    total_revenue,
    frequency_score,
    monetary_score,

    CASE
        WHEN frequency_score >= 4
         AND monetary_score >= 4
        THEN 'High Value'

        WHEN frequency_score >= 3
         AND monetary_score >= 3
        THEN 'Mid Value'

        ELSE 'Low Value'
    END AS customer_value_segment

FROM rfm_scores

ORDER BY total_revenue DESC;
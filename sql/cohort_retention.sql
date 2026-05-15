WITH first_purchase AS (

    SELECT
        customer_id,
        MIN(order_date) AS first_order_date
    FROM orders
    GROUP BY customer_id
),

orders_with_cohort AS (

    SELECT
        o.customer_id,
        o.order_id,
        o.order_date,

        strftime('%Y-%m', fp.first_order_date) AS cohort_month,
        strftime('%Y-%m', o.order_date) AS order_month,

        (
            (CAST(strftime('%Y', o.order_date) AS INTEGER) -
             CAST(strftime('%Y', fp.first_order_date) AS INTEGER)) * 12
        )
        +
        (
            CAST(strftime('%m', o.order_date) AS INTEGER) -
            CAST(strftime('%m', fp.first_order_date) AS INTEGER)
        ) AS cohort_index

    FROM orders o

    JOIN first_purchase fp
        ON o.customer_id = fp.customer_id
),

cohort_data AS (

    SELECT
        cohort_month,
        cohort_index,
        COUNT(DISTINCT customer_id) AS active_customers
    FROM orders_with_cohort
    GROUP BY
        cohort_month,
        cohort_index
),

cohort_size AS (

    SELECT
        cohort_month,
        active_customers AS cohort_customers
    FROM cohort_data
    WHERE cohort_index = 0
)

SELECT
    cd.cohort_month,
    cd.cohort_index,
    cd.active_customers,
    cs.cohort_customers,

    ROUND(
        cd.active_customers * 1.0 / cs.cohort_customers,
        4
    ) AS retention_rate

FROM cohort_data cd

JOIN cohort_size cs
    ON cd.cohort_month = cs.cohort_month

ORDER BY
    cd.cohort_month,
    cd.cohort_index;
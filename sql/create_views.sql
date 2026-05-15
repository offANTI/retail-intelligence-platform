DROP VIEW IF EXISTS vw_monthly_revenue;
DROP VIEW IF EXISTS vw_category_performance;
DROP VIEW IF EXISTS vw_customer_segment_revenue;
DROP VIEW IF EXISTS vw_return_rate_by_category;

CREATE VIEW vw_monthly_revenue AS
SELECT
    strftime('%Y-%m', o.order_date) AS order_month,
    ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS revenue,
    COUNT(DISTINCT o.order_id) AS total_orders,
    ROUND(
        SUM(oi.quantity * oi.unit_price * (1 - oi.discount))
        / COUNT(DISTINCT o.order_id),
        2
    ) AS average_order_value
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY order_month;


CREATE VIEW vw_category_performance AS
SELECT
    p.category,
    ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS revenue,
    ROUND(SUM(oi.quantity * (oi.unit_price * (1 - oi.discount) - p.cost_price)), 2) AS gross_margin,
    ROUND(
        SUM(oi.quantity * (oi.unit_price * (1 - oi.discount) - p.cost_price))
        / SUM(oi.quantity * oi.unit_price * (1 - oi.discount)),
        4
    ) AS gross_margin_rate,
    SUM(oi.quantity) AS units_sold
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY p.category;


CREATE VIEW vw_customer_segment_revenue AS
SELECT
    c.customer_segment,
    ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS revenue,
    COUNT(DISTINCT c.customer_id) AS customers,
    COUNT(DISTINCT o.order_id) AS orders,
    ROUND(
        SUM(oi.quantity * oi.unit_price * (1 - oi.discount))
        / COUNT(DISTINCT c.customer_id),
        2
    ) AS revenue_per_customer
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY c.customer_segment;


CREATE VIEW vw_return_rate_by_category AS
SELECT
    p.category,
    COUNT(r.return_id) AS returned_items,
    COUNT(oi.order_item_id) AS sold_items,
    ROUND(COUNT(r.return_id) * 1.0 / COUNT(oi.order_item_id), 4) AS return_rate
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
LEFT JOIN returns r
    ON oi.order_item_id = r.order_item_id
GROUP BY p.category;
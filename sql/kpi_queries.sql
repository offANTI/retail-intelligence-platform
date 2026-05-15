SELECT 'customers' AS table_name, COUNT(*) AS row_count FROM customers
UNION ALL
SELECT 'products', COUNT(*) FROM products
UNION ALL
SELECT 'orders', COUNT(*) FROM orders
UNION ALL
SELECT 'order_items', COUNT(*) FROM order_items
UNION ALL
SELECT 'returns', COUNT(*) FROM returns;



SELECT
    ROUND(SUM(quantity * unit_price * (1 - discount)), 2) AS total_revenue
FROM order_items;



SELECT
    p.category,
    ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS revenue
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;



SELECT
    p.category,
    ROUND(SUM(oi.quantity * (oi.unit_price * (1 - oi.discount) - p.cost_price)), 2) AS gross_margin,
    ROUND(
        SUM(oi.quantity * (oi.unit_price * (1 - oi.discount) - p.cost_price))
        / SUM(oi.quantity * oi.unit_price * (1 - oi.discount)),
        4
    ) AS gross_margin_rate
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY p.category
ORDER BY gross_margin DESC;



SELECT
    strftime('%Y-%m', o.order_date) AS order_month,
    ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS revenue
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY order_month
ORDER BY order_month;



SELECT
    p.product_name,
    p.category,
    ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS revenue
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY p.product_id, p.product_name, p.category
ORDER BY revenue DESC
LIMIT 10;



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
GROUP BY p.category
ORDER BY return_rate DESC;
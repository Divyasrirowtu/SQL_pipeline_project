-- Q1: Total number of users
SELECT COUNT(*) AS total_users FROM users;

-- Q2: Total revenue
SELECT SUM(total_amount) AS total_revenue FROM orders;

-- Q3: Top 10 products by revenue
SELECT p.product_id, p.name, SUM(o.total_amount) AS revenue
FROM products p
JOIN orders o ON p.product_id = o.product_id
GROUP BY p.product_id, p.name
ORDER BY revenue DESC
LIMIT 10;

-- Q4: Top 10 users by total spend
SELECT u.user_id, u.name, SUM(o.total_amount) AS spend
FROM users u
JOIN orders o ON u.user_id = o.user_id
GROUP BY u.user_id, u.name
ORDER BY spend DESC
LIMIT 10;

-- Q5: Monthly revenue
WITH monthly_revenue AS (
    SELECT DATE_TRUNC('month', order_date) AS month,
           SUM(total_amount) AS revenue
    FROM orders
    GROUP BY month
)
SELECT *,
       revenue - LAG(revenue) OVER (ORDER BY month) AS growth
FROM monthly_revenue;

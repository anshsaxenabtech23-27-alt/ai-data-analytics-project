-- Active: 1789559202723@@127.0.0.1@3306@ecommerce
USE ecommerce;
SELECT p.product_name, SUM(o.quantity) AS total_sold
FROM Orders o
JOIN Products p ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC;

--- monthly revenue---
SELECT MONTH(order_date) AS month, SUM(p.price * o.quantity) AS revenue
FROM Orders o
JOIN Products p ON o.product_id = p.product_id
GROUP BY MONTH(order_date);

--- customer orders count---
SELECT c.name, COUNT(o.order_id) AS total_orders
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.name;
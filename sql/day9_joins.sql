-- Create products table
CREATE TABLE products (
    product_id INT,
    product_name TEXT,
    price INT
);

-- Create orders table
CREATE TABLE orders (
    order_id INT,
    product_id INT,
    quantity INT
);

-- Insert data into products
INSERT INTO products VALUES
(1, 'Phone', 20000),
(2, 'Laptop', 50000),
(3, 'Earphones', 2000);

-- Insert data into orders
INSERT INTO orders VALUES
(101, 1, 2),
(102, 2, 1),
(103, 3, 3);

-- JOIN query
SELECT 
    o.order_id,
    p.product_name,
    p.price,
    o.quantity,
    (p.price * o.quantity) AS revenue
FROM orders o
JOIN products p
ON o.product_id = p.product_id;

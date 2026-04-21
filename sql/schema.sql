-- ORDERS TABLE
CREATE TABLE orders (
    order_id TEXT PRIMARY KEY,
    customer_id TEXT,
    order_status TEXT,
    order_purchase_timestamp TIMESTAMP,
    order_delivered_customer_date TIMESTAMP
);

-- ORDER ITEMS TABLE
CREATE TABLE order_items (
    order_id TEXT,
    order_item_id INT,
    product_id TEXT,
    seller_id TEXT,
    price FLOAT,
    freight_value FLOAT
);

-- PRODUCTS TABLE
CREATE TABLE products (
    product_id TEXT PRIMARY KEY,
    product_category_name TEXT
);
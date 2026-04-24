-- sql/schema.sql

CREATE TABLE IF NOT EXISTS customers (
    customer_id             VARCHAR(50) PRIMARY KEY,
    customer_unique_id      VARCHAR(50),
    customer_zip_code_prefix VARCHAR(10),
    customer_city           VARCHAR(100),
    customer_state          VARCHAR(5)
);

CREATE TABLE IF NOT EXISTS sellers (
    seller_id               VARCHAR(50) PRIMARY KEY,
    seller_zip_code_prefix  VARCHAR(10),
    seller_city             VARCHAR(100),
    seller_state            VARCHAR(5)
);

CREATE TABLE IF NOT EXISTS products (
    product_id                      VARCHAR(50) PRIMARY KEY,
    product_category_name           VARCHAR(100),
    product_category_name_english   VARCHAR(100),
    product_name_lenght             INTEGER,  
    product_description_lenght      INTEGER,   
    product_photos_qty              INTEGER,
    product_weight_g                NUMERIC,
    product_length_cm               NUMERIC,
    product_height_cm               NUMERIC,
    product_width_cm                NUMERIC
);

CREATE TABLE IF NOT EXISTS orders (
    order_id                        VARCHAR(50) PRIMARY KEY,
    customer_id                     VARCHAR(50) REFERENCES customers(customer_id),
    order_status                    VARCHAR(30),
    order_purchase_timestamp        TIMESTAMP,
    order_approved_at               TIMESTAMP,
    order_delivered_carrier_date    TIMESTAMP,
    order_delivered_customer_date   TIMESTAMP,
    order_estimated_delivery_date   TIMESTAMP
);

CREATE TABLE IF NOT EXISTS order_items (
    order_id            VARCHAR(50) REFERENCES orders(order_id),
    order_item_id       INTEGER,
    product_id          VARCHAR(50) REFERENCES products(product_id),
    seller_id           VARCHAR(50) REFERENCES sellers(seller_id),
    shipping_limit_date TIMESTAMP,
    price               NUMERIC,
    freight_value       NUMERIC,
    PRIMARY KEY (order_id, order_item_id)
);

CREATE TABLE IF NOT EXISTS payments (
    order_id                VARCHAR(50) REFERENCES orders(order_id),
    payment_sequential      INTEGER,
    payment_type            VARCHAR(30),
    payment_installments    INTEGER,
    payment_value           NUMERIC,
    PRIMARY KEY (order_id, payment_sequential)
);

CREATE TABLE IF NOT EXISTS reviews (
    review_id               VARCHAR(50) PRIMARY KEY,
    order_id                VARCHAR(50) REFERENCES orders(order_id),
    review_score            INTEGER,
    review_comment_title    TEXT,
    review_comment_message  TEXT,
    review_creation_date    TIMESTAMP,
    review_answer_timestamp TIMESTAMP
);

CREATE TABLE IF NOT EXISTS geolocation (
    geolocation_zip_code_prefix VARCHAR(10) PRIMARY KEY,
    geolocation_lat             NUMERIC,
    geolocation_lng             NUMERIC,
    geolocation_city            VARCHAR(100),
    geolocation_state           VARCHAR(5)
);
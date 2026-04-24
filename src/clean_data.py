# src/clean_data.py
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW   = os.path.join(BASE_DIR, "data", "raw") + os.sep
CLEAN = os.path.join(BASE_DIR, "data", "cleaned") + os.sep
os.makedirs(CLEAN, exist_ok=True)

# ORDERS
orders = pd.read_csv(RAW + "olist_orders_dataset.csv")

# Convert datetime
date_cols = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]
for col in date_cols:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")

# useful order statuses

print("Order statuses:", orders["order_status"].value_counts().to_dict())

orders.to_csv(CLEAN + "orders.csv", index=False)
print(f"✅ orders cleaned → {len(orders)} rows")


#  ORDER ITEMS 
items = pd.read_csv(RAW + "olist_order_items_dataset.csv")

items["shipping_limit_date"] = pd.to_datetime(
    items["shipping_limit_date"], errors="coerce"
)

# price and freight_value = float
items["price"] = pd.to_numeric(items["price"], errors="coerce")
items["freight_value"] = pd.to_numeric(items["freight_value"], errors="coerce")

# Drop rows  price null 
before = len(items)
items.dropna(subset=["price"], inplace=True)
print(f"  Dropped {before - len(items)} rows with null price")

items.to_csv(CLEAN + "order_items.csv", index=False)
print(f"✅ order_items cleaned → {len(items)} rows")


#  PAYMENTS 
payments = pd.read_csv(RAW + "olist_order_payments_dataset.csv")

payments["payment_value"] = pd.to_numeric(
    payments["payment_value"], errors="coerce"
)
payments.dropna(subset=["payment_value"], inplace=True)

payments.to_csv(CLEAN + "payments.csv", index=False)
print(f"✅ payments cleaned → {len(payments)} rows")


#  PRODUCTS 
products = pd.read_csv(RAW + "olist_products_dataset.csv")
translation = pd.read_csv(RAW + "product_category_name_translation.csv")

# Merge to get English category 
products = products.merge(translation, on="product_category_name", how="left")

# Fill missing category names
products["product_category_name_english"].fillna("unknown", inplace=True)

# Fill missing dimen/wei with reasonable assumption
for col in ["product_weight_g", "product_length_cm",
            "product_height_cm", "product_width_cm"]:
    products[col] = pd.to_numeric(products[col], errors="coerce")
    products[col].fillna(products[col].median(), inplace=True)

products.to_csv(CLEAN + "products.csv", index=False)
print(f"✅ products cleaned → {len(products)} rows")


#  CUSTOMERS 
customers = pd.read_csv(RAW + "olist_customers_dataset.csv")
# This one is fairly clean
print(f"  Customer nulls:\n{customers.isnull().sum()}")
customers.to_csv(CLEAN + "customers.csv", index=False)
print(f"✅ customers cleaned → {len(customers)} rows")


# REVIEWS 
reviews = pd.read_csv(RAW + "olist_order_reviews_dataset.csv")

reviews["review_comment_message"].fillna("", inplace=True)
reviews["review_comment_title"].fillna("", inplace=True)

date_cols = ["review_creation_date", "review_answer_timestamp"]
for col in date_cols:
    reviews[col] = pd.to_datetime(reviews[col], errors="coerce")

#
before = len(reviews)
reviews.drop_duplicates(subset=["review_id"], inplace=True)
print(f"  Reviews: removed {before - len(reviews)} duplicate review_ids")

reviews.to_csv(CLEAN + "reviews.csv", index=False)
print(f"✅ reviews cleaned → {len(reviews)} rows")


#  SELLERS 
sellers = pd.read_csv(RAW + "olist_sellers_dataset.csv")
sellers.to_csv(CLEAN + "sellers.csv", index=False)
print(f"✅ sellers cleaned → {len(sellers)} rows")


#  GEOLOCATION 
geo = pd.read_csv(RAW + "olist_geolocation_dataset.csv")


before = len(geo)
geo.drop_duplicates(subset=["geolocation_zip_code_prefix"], inplace=True)
print(f"  Geolocation: {before} → {len(geo)} rows after dedup")

geo.to_csv(CLEAN + "geolocation.csv", index=False)
print(f"✅ geolocation cleaned → {len(geo)} rows")

print("\n🎉 All files cleaned and saved to data/cleaned/")
# src/load_data.py
import pandas as pd
import os
from db_connection import get_connection

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


CSV_FILES = {
    "customers":   os.path.join(BASE_DIR, "data", "cleaned", "customers.csv"),
    "sellers":     os.path.join(BASE_DIR, "data", "cleaned", "sellers.csv"),
    "products":    os.path.join(BASE_DIR, "data", "cleaned", "products.csv"),
    "orders":      os.path.join(BASE_DIR, "data", "cleaned", "orders.csv"),
    "order_items": os.path.join(BASE_DIR, "data", "cleaned", "order_items.csv"),
    "payments":    os.path.join(BASE_DIR, "data", "cleaned", "payments.csv"),
    "reviews":     os.path.join(BASE_DIR, "data", "cleaned", "reviews.csv"),
    "geolocation": os.path.join(BASE_DIR, "data", "cleaned", "geolocation.csv"),
}

def load_table(cursor, table_name, filepath):
    print(f"\n⏳ Loading {table_name}...")

    df = pd.read_csv(filepath)

  
    columns = ", ".join([f'"{col}"' for col in df.columns])
    placeholders = ", ".join(["%s"] * len(df.columns))

    insert_query = f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})'

    
    rows = [
        tuple(None if pd.isna(v) else v for v in row)
        for _, row in df.iterrows()
    ]

    cursor.executemany(insert_query, rows)
    print(f"  ✅ {table_name} — {len(rows)} rows inserted")


def load_all():
    conn = get_connection()
    if not conn:
        print("❌ No connection, aborting.")
        return

    cursor = conn.cursor()

    try:
        for table_name, filepath in CSV_FILES.items():

           
            if not os.path.exists(filepath):
                print(f"  ⚠️  File not found, skipping: {filepath}")
                continue

            load_table(cursor, table_name, filepath)
            conn.commit()  # commit after each table

    except Exception as e:
        conn.rollback()  # rollback everything 
        print(f"\n❌ Error: {e}")

    finally:
        cursor.close()
        conn.close()
        print("\n🎉 Done loading all tables!")


if __name__ == "__main__":
    load_all()
import os
import psycopg2
from db_connection import get_connection

def run_sql_file(filename):
    base_path = r"C:\Users\josel\PhyPrjts\Revenue Leak Detector\sql"
    filepath = os.path.join(base_path, filename)
    
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        if not os.path.exists(filepath):
            print(f"Error: The file {filepath} was not found.")
            return

        with open(filepath, "r") as f:
            sql = f.read()

        queries = [q.strip() for q in sql.split(";") if q.strip()]
        
        for query in queries:

            display_query = query.replace('\n', ' ').strip()
            print(f"Executing: {display_query[:50]}...")
            
            try:
                cursor.execute(query)
                
                if cursor.description is not None:
                    results = cursor.fetchall()
                    for row in results:
                        print(f"  Result: {row}")
                else:
                    print("  Command executed successfully (no rows returned).")
            
            except psycopg2.Error as e:
                print(f"  SQL Error executing query: {e}")
                conn.rollback()
                continue

        conn.commit()
        print("\nAll queries committed successfully.")

    except Exception as e:
        print(f"General Error: {e}")
    
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    run_sql_file("schema.sql")
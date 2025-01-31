import os
import sys
import psycopg2
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

def create_tables():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD,
            host=DB_HOST, port=DB_PORT
        )
        cur = conn.cursor()

        create_books_table = """
         CREATE TABLE IF NOT EXISTS books (
            id SERIAL PRIMARY KEY,
            isbn VARCHAR(20),
            title TEXT UNIQUE NOT NULL,
            authors TEXT[],
            publish_date TEXT,
            subjects TEXT[],
            page_count INT
        );
        """
        
        cur.execute(create_books_table)
        conn.commit()
        cur.close()
        conn.close()
        print("✅ Tables created successfully!")

    except Exception as e:
        print("❌ Error creating tables:", e)

if __name__ == "__main__":
    create_tables()
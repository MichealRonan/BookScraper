import psycopg2
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
from fetch_books import fetch_books

def store_books_in_db(books):
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD,
            host=DB_HOST, port=DB_PORT
        )
        cur = conn.cursor()

        insert_query = """
        INSERT INTO books (isbn, title, authors, publish_date, subjects, page_count)
        VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (title) DO NOTHING;
        """
        
        for book in books:
            cur.execute(insert_query, (
                book["isbn"],
                book["title"],
                book["authors"],
                book["publish_date"],
                book["subjects"],
                book["page_count"]
            ))

        conn.commit()
        cur.close()
        conn.close()
        print(f"✅ {len(books)} books stored.")

    except Exception as e:
        print("Error inserting data:", e)

if __name__ == "__main__":
    books = fetch_books()  # Fetches books before storing
    store_books_in_db(books)
import requests
import json

def get_books_by_subject(subject, limit=50):
    url = f"https://openlibrary.org/subjects/{subject}.json?limit={limit}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"⚠️ Failed to fetch books for subject: {subject}")
        return []

    data = response.json()
    books = []

    for doc in data.get("works", []):  # Using `.get()` prevents KeyError crashes
        book_details = {
            "isbn": doc.get("cover_edition_key", f"NO_ISBN_{doc['key']}"),  # Handle missing ISBNs
            "title": doc.get("title", "N/A"),
            "authors": [author["name"] for author in doc.get("authors", [])],
            "publish_date": doc.get("first_publish_year", "Unknown"), 
            "subjects": [subject],
            "page_count": 0  # Might try add this later, not reliable right now
        }
        books.append(book_details)

    return books

def fetch_books():
    subject_list = ["fantasy", "epic_fantasy", "dark_fantasy", "urban_fantasy",
                    "mythology", "sword_and_sorcery", "magical_realism", "steampunk",
                    "high_fantasy", "low_fantasy", "fairy_tales", "supernatural",
                    "isekai", "action", "adventure", "martial_arts", "military",
                    "thriller", "superheroes", "war", "spy_fiction", "dystopian",
                    "post_apocalyptic", "time_travel", "wuxia"]

    all_books = []
    for subject in subject_list:
        books = get_books_by_subject(subject, limit=50)
        all_books.extend(books)

    return all_books
if __name__ == "__main__":
    books = fetch_books()
    print(json.dumps(books, indent=4))
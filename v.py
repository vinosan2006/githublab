import json
import os

FILE_NAME = "library_data.json"

# -------------------- Data Handling --------------------

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_data(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)

# -------------------- Book Functions --------------------

def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")

    book = {
        "title": title,
        "author": author,
        "year": year,
        "available": True
    }

    books.append(book)
    save_data(books)
    print("✅ Book added successfully!")

def view_books(books):
    if not books:
        print("📭 No books in the library.")
        return

    print("\n📚 Library Books:")
    for i, book in enumerate(books, start=1):
        status = "Available" if book["available"] else "Borrowed"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {status}")

def borrow_book(books):
    view_books(books)
    if not books:
        return

    choice = int(input("Enter book number to borrow: ")) - 1
    if 0 <= choice < len(books):
        if books[choice]["available"]:
            books[choice]["available"] = False
            save_data(books)
            print("📕 You borrowed the book!")
        else:
            print("❌ Book is already borrowed.")
    else:
        print("❌ Invalid choice.")

def return_book(books):
    view_books(books)
    if not books:
        return

    choice = int(input("Enter book number to return: ")) - 1
    if 0 <= choice < len(books):
        if not books[choice]["available"]:
            books[choice]["available"] = True
            save_data(books)
            print("📗 Book returned successfully!")
        else:
            print("❌ This book was not borrowed.")
    else:
        print("❌ Invalid choice.")

def search_book(books):
    keyword = input("Enter title or author to search: ").lower()
    found = False

    for book in books:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            status = "Available" if book["available"] else "Borrowed"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {status}")
            found = True

    if not found:
        print("🔍 No matching books found.")

# -------------------- Menu --------------------

def menu():
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")

# -------------------- Main Program --------------------

def main():
    books = load_data()

    while True:
        menu()
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            borrow_book(books)
        elif choice == "4":
            return_book(books)
        elif choice == "5":
            search_book(books)
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()

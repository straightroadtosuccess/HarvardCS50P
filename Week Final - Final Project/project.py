import json
import os
import csv


BOOKS_FILE = "books.json"
# Global list
books = []


def load_books():
    if not os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "w") as f:
            # Create empty list only if file doesn't exist
            json.dump([], f)

    with open(BOOKS_FILE, "r") as f:
        try:
            loaded_books = json.load(f)
            print(f"Loaded {len(loaded_books)} book(s)")
            return loaded_books
        except json.JSONDecodeError:
            # Safe fallback if corrupted file
            return []


def save_books():
    global books
    # Write the current list of books
    with open(BOOKS_FILE, "w") as f:
        json.dump(books, f, indent=2)


def main():
    global books
    # Load existing books from file
    books = load_books()

    # Show options to choose from
    print("\n BOOK LIST TRACKER \n")
    print("1. Add a book ")
    print("2. Mark book as read ")
    print("3. Filter books ")
    print("4. List books ")
    print("5. Export books list ")

    # Get input from the user
    choice = input("\nWhat do you want to do? ")

    # From user input, do one of the following
    if choice == "1":
        add_book()
        save_books()
    elif choice == "2":
        mark_read()
        save_books()
    elif choice == "3":
        filtered = filter_books()
        list_books(filtered)
    elif choice == "4":
        list_books()
    elif choice == "5":
        export_books_to_csv()
    elif choice == "book":
        print("Then Yes")
    elif choice == "6":
        print("No")
    else:
        print("\nInvalid choice ")


def add_book():
    global books
    # Get input from user
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    read = input("Have you read it? (y/n) ").strip().lower()

    # Create a new dict
    book = {
        "title": title,
        "author": author,
        "read": read == "y",
    }

    # Add the new book to global books
    books.append(book)
    print(f"\n{title} added!")


def mark_read():
    global books
    # Ask user if they want to mark book as read
    title = input("Enter title of book you have read: ").strip()
    found = False

    # Search through books by title
    for book in books:
        if book["title"].lower() == title.lower():
            read_status = input("Mark as read? (y/n): ").strip().lower()
            book["read"] = read_status == "y"
            print(f"Updated {book['title']} to read: {book['read']}")
            found = True
            break

    # If no match book, no book
    if not found:
        print("\nBook not found ")


def filter_books():
    global books
    # Ask user for author to filter
    author_filter = input("Filter by author: ").strip().lower()

    # Index for filtered
    filtered = []

    # Loop through all books and show those matching filter
    for book in books:
        if author_filter and author_filter not in book["author"].lower():
            continue
        filtered.append(book)

    # Show by alphabetical order
    filtered.sort(key=lambda b: b["title"].lower())
    return filtered


def list_books(book_list=None):
    global books
    # If no list given, use full global list
    if book_list is None:
        book_list = books

    # If still empty, show message
    if not book_list:
        print("\nNo books ")
        return

    # Loop through and show info
    for book in book_list:
        # Print book details
        print(f"\nTitle: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Read: {'Yes' if book['read'] else 'No'}")
        print()


def export_books_to_csv():
    global books
    # If book list empty, tell user and stop
    if not books:
        print("\nNo books to export ")
        return

    # Export to csv file
    filename = "books_export.csv"

    # Open file for writing, create new file if not there and overwrite
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        # Create csv writer with these new columns
        writer = csv.DictWriter(csvfile, fieldnames=["title", "author", "read"])
        writer.writeheader()
        for book in books:
            # Write each book as a row in csv
            writer.writerow({
                "title": book["title"],
                "author": book["author"],
                # Convert to yes or no
                "read": "Yes" if book["read"] else "No"
            })

    # Print the result!
    print(f"\nExported to books_export.csv")


if __name__ == "__main__":
    main()

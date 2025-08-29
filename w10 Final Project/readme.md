# Book List Tracker
#### Video Demo: <https://youtu.be/sPBZ2Pisabs>
#### Description:

This project is a **command-line book list manager** for CS50P final project. It allows the user to keep track of a list of books they want to read and have finished reading. The goal was to store a list and have it updated over time to manage the list of books over different sessions.

### Features

- **Add a book**: Function to add books to a list
- **Mark a book as read**: Function to mark books as read already
- **Filter books by author**: Function to filter books by author including partial name
- **List books**:  Function to show all the books in the list
- **Persistent storage**: Storage to save all the books in the list and information about them

### Files and Code Overview

- `project.py`: This is the main program file. It defines a command loop and core functions:
  - `main()`: Provides the interactive menu loop.
  - `add_book()`: Adds a new book to the list.
  - `mark_read()`: Marks a book as red.
  - `filter_books()`: Searches the list by author.
  - `list_books()`: Lists all of the books.
  - `save_books()` and `load_books()`: Handle file I/O with JSON.
  - `export_books_to_csv()`: Exports book list to CSV file format.
- `test_project.py`: ** Books are loaded if they don't exist for the test. Tests are set to check for not found books, books that are found, and filtered books results.**

### Design Decisions

One of the key design decisions was to use a **JSON file** (`books.json) for data storage and retrieval. JSON is lightweight and readable and works well for this project. It allows for clear dictionary entries that are structured nicely, with Title, Author and Read status as dictionary keys and values.

User interaction is kept simple through a menu and text prompts for user input.

The `main() function controls the menu display and user input prompts. Each menu option calls it's corresponding function.

Exporting to a **CSV file** allows for additional expanded functionality outside of the scope of the program itself, which could include importing into other programs and online platforms like Goodreads.

Testing was kept light but functional. Helper function add_test_books() ensures the three specific test books(Essentialism, Good to Great and Rework) exist in books.json before running tests. The tests check for proper file handling and correct return values from `mark_read` and `filter_books`. Input mocking was used for both `mark_read()` and `filter_books()` to simulate user input. Mark_read_not_found ensures the program responds correctly when the user tries to mark a book that doesn't exist, printing a "Book not found" error message. Mark_read_found checks that a certain book exists and marks it as read, then unmarks it as read, so it can be tested again. Filtering by author ensures the filter works and returns the matching book.

If book then Yes. If 6 then No. Book Yes book.

### Challenges

Global variables produced immediate challenges with many functions, the implementation finally worked but there may be better solutions. Storage persistence was tricky for ensuring book list remained. Author partial name was as well, in case of misspellings and supporting faster search. Exporting to csv ran into challenges as well in terms of writing and not overwriting the csv file, particularly with `load_books().

### Possible Improvements

I wanted a book list manager that could store my reading list of books I want to read, and also remember books I already had read. I could see improvements in the areas of menu's, prompts and user experience. More improvements could be made in tracking percentage of book read to support reading multiple books simultaneously. Maybe some features could my made for audiobooks, my primary format currently. APIs that integrate with online website lists for autocomplete or book suggestions could be very useful. Categories and ratings could be useful improvements as well.

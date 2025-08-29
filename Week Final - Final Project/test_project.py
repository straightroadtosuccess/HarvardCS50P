import project
import sys
from io import StringIO


# --- helper ---
def add_test_books():
    required_books = [
        {"title": "Essentialism", "author": "Greg McKeown", "read": True},
        {"title": "Good to Great", "author": "Jim Collins", "read": False},
        {"title": "Rework", "author": "Jason Fried", "read": False}
    ]

    books = project.load_books()
    for book in required_books:
        if not any(b["title"].lower() == book["title"].lower() for b in books):
            books.append(book)

    project.books = books
    project.save_books()


# --- tests ---
def test_mark_read_not_found(monkeypatch):
    project.books = [{"title": "The Lord of The Rings Trilogy", "author": "J.R.R. Tolkien", "read": True}]
    monkeypatch.setattr('builtins.input', lambda _: "Nonexistent")
    captured_output = StringIO()
    sys.stdout = captured_output
    project.mark_read()
    sys.stdout = sys.__stdout__
    assert "Book not found" in captured_output.getvalue()


def test_mark_read_found(monkeypatch):
    add_test_books()
    project.books = [{"title": "Rework", "author": "Jason Fried", "read": False}]

    # Mark as read
    inputs = iter(["Rework", "y"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    project.mark_read()

    # Mark as unread again
    inputs = iter(["Rework", "n"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    project.mark_read()
    assert project.books[0]["read"] is False


def test_filter_books(monkeypatch):
    add_test_books()
    project.books = [
        {"title": "Essentialism", "author": "Greg McKeown", "read": True},
        {"title": "Good to Great", "author": "Jim Collins", "read": False},
    ]
    monkeypatch.setattr("builtins.input", lambda _: "Collins")
    assert project.filter_books()[0]["title"] == "Good to Great"

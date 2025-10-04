class Book:
    """Represents a book with a title, author, and availability status."""

    def __init__(self, title, author):
        """Initialize a new book with title and author. Default: not checked out."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
        else:
            print(f"'{self.title}' is already checked out.")

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
        else:
            print(f"'{self.title}' was not checked out.")

    def is_available(self):
        """Return True if the book is available, False otherwise."""
        return not self._is_checked_out


class Library:
    """Represents a collection of books and provides methods to manage them."""

    def __init__(self):
        """Initialize an empty library."""
        self._books = []

    def add_book(self, book):
        """Add a Book object to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Mark a book as checked out by title."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        """Return a book (make it available again) by title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        """Print the list of all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")

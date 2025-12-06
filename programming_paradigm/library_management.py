"""
Implements the Book and Library classes for a basic library management system,
demonstrating OOP concepts like classes, attributes, and methods.
"""

class Book:
    """
    Represents a book with a title, author, and availability status.
    """

    def __init__(self, title, author):
        """Initializes a new Book instance."""
        # Public attributes
        self.title = title
        self.author = author
        # Private attribute (conventionally indicated by a single leading underscore)
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out (unavailable)."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # Already checked out

    def return_book(self):
        """Marks the book as available (returned)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # Already available (error state)

    def is_available(self):
        """Returns the current availability status of the book."""
        return not self._is_checked_out

    def __str__(self):
        """Returns a user-friendly string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of books and their lending operations.
    """

    def __init__(self):
        """Initializes a new Library with an empty list of books."""
        # Private attribute (conventionally indicated by a single leading underscore)
        self._books = []

    def add_book(self, book):
        """Adds a Book object to the library's collection."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print(f"Error: {book} is not a valid Book object.")

    def _find_book(self, title):
        """Helper method to find a book object by title."""
        # Find the first book object matching the title
        for book in self._books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title):
        """Finds a book by title and checks it out if available."""
        book = self._find_book(title)
        if book:
            if book.check_out():
                print(f"'{title}' has been checked out.")
            else:
                print(f"'{title}' is already checked out.")
        else:
            print(f"Error: Book titled '{title}' not found in library.")

    def return_book(self, title):
        """Finds a book by title and returns it if checked out."""
        book = self._find_book(title)
        if book:
            if book.return_book():
                print(f"'{title}' has been returned.")
            else:
                print(f"'{title}' was already available.")
        else:
            print(f"Error: Book titled '{title}' not found in library.")

    def list_available_books(self):
        """Prints the title and author of all books currently available."""
        available_found = False
        for book in self._books:
            if book.is_available():
                print(book) # Uses the Book's __str__ method
                available_found = True
        
        if not available_found:
             print("No books are currently available.")

# You should save the main.py provided in the prompt separately 
# and use it to test this library_management.py file.

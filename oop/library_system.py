class Book:
    def __init__(self, title, author):
        """
        Base Book class
        """
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title, author, file_size):
        """
        EBook inherits from Book
        """
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """
        PrintBook inherits from Book
        """
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    def __init__(self):
        """
        Library uses composition to store books
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a book to the library
        """
        self.books.append(book)

    def list_books(self):
        """
        Lists all books in the library
        """
        for book in self.books:
            if isinstance(book, EBook):
                print(
                    f"EBook: {book.title} by {book.author}, "
                    f"File Size: {book.file_size}KB"
                )
            elif isinstance(book, PrintBook):
                print(
                    f"PrintBook: {book.title} by {book.author}, "
                    f"Page Count: {book.page_count}"
                )
            else:
                print(f"Book: {book.title} by {book.author}")

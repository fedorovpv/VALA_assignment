import os
from typing import List
from libraries.Book import Book


class Library:
    """Manages a collection of books stored in a file."""
    def __init__(self, filename: str):
        """
        Initializes the Library instance and loads books from the given file.

        Parameters:
            filename: path to text file for library.
        """
        self.filename = filename
        self.books = self.load_books()

    def add_book(self, new_book: Book) -> None:
        """Adds a new book to the library and saves it to the file."""
        self.books.append(new_book)
        self.books.sort(key=lambda a: a.year)
        self.save_library()

    def save_library(self) -> None:
        """Saves the current list of books to the file."""
        with open(self.filename, 'w') as f:
            for book in self.books:
                f.write(book.get_line_for_storage() + '\n')

    def load_books(self) -> List[Book]:
        """Loads library from a file."""
        books = []
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                for line in f:
                    try:
                        title, author, isbn, year = line.strip().split('/')
                        books.append(Book(title=title, author=author, isbn=isbn, year=int(year)))
                    except ValueError:
                        print(f"Error during reading library file. Skipping invalid line: {line.strip()}")
        return books

from dataclasses import dataclass


@dataclass
class Book:
    """
    Represents a single book in the library.

    Parameters:
        title (str): The title of the book.
        author (str): The author's name.
        isbn (str): The book's ISBN number.
        year (int): The year the book was published.
    """
    title: str
    author: str
    isbn: str
    year: int

    def __str__(self):
        """Returns a human-readable string representation of the book."""
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Year: {self.year}"

    def get_line_for_storage(self):
        """Returns a string suitable for saving the book to a file."""
        return f"{self.title}/{self.author}/{self.isbn}/{self.year}"

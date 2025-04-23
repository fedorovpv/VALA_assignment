from libraries.Book import Book
from libraries.Library import Library


class Menu:
    """Provides a text-based user interface for interacting with the library."""
    def __init__(self, library: Library):
        """
        Initializes the Menu with a given Library instance.

        Parameters:
            library: Library instance to operate on.
        """
        self.library = library

    def print_headliner(self, headliner: str) -> None:
        """Prints a centered headline with decorative padding."""
        print()
        headliner_len = len(headliner)
        padding_len = (106 - headliner_len) // 2
        padding = '#' * padding_len
        print(f"{padding}  {headliner}  {padding}")

    def main_menu(self) -> None:
        """Displays the main menu and processes user choices."""
        while True:
            self.print_headliner('MAIN MENU')
            print("1. Add new book")
            print("2. Print all books")
            print("Q. Quit")

            choice = input("Select an option: ").strip().lower()

            if choice == '1':
                self.add_book_dialog()
            elif choice == '2':
                self.print_all_books()
            elif choice == 'q':
                self.print_headliner('GOODBYE!')
                break
            else:
                print("Unsupported option. Please, use '1', '2' or 'Q'.")

    def add_book_dialog(self) -> None:
        """Handles user input for adding a new book"""
        self.print_headliner('ADDING NEW BOOK')
        title = input("Title: ").strip()
        author = input("Author: ").strip()
        isbn = input("ISBN: ").strip()
        year = input("Year: ").strip()

        while not year.isdigit():
            print("Error. Year should be integer.")
            year = input("Year: ").strip()
        new_book = Book(
            title=title,
            author=author,
            isbn=isbn,
            year=int(year)
        )

        print("\nBook to add:")
        print(new_book)
        confirm = input("Do you want to add this book to the database? (y/n): ").strip().lower()
        if confirm == 'y':
            self.library.add_book(new_book)
            print("Book was added.")
        else:
            print("Book was not added.")

    def print_all_books(self) -> None:
        """Prints all books in the library in a formatted table."""
        self.print_headliner('LIBRARY BOOKS')
        print(f"{'Title':<50} {'Author':<25} {'ISBN':<20} {'Year':<4}")
        print("-" * 110)
        for book in self.library.books:
            print(f"{book.title:<50} {book.author:<25} {book.isbn:<20} {book.year:<4}")

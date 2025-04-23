import sys
from libraries.Library import Library
from libraries.Menu import Menu


def parse_parameters():
    if len(sys.argv) < 2:
        raise ValueError(
            "ERROR: library filename was not provided. \n"
            "Usage: python my_library_db.py <library_file>")

    filepath = sys.argv[1]
    return filepath


if __name__ == "__main__":
    filename = parse_parameters()
    library = Library(filename=filename)
    Menu(library).main_menu()

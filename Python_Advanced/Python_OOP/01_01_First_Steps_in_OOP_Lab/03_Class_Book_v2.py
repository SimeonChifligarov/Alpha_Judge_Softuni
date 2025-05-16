class Book:
    """
    A class that represents a book with a name, author, and number of pages.

    Args:
        name: the title of the book
        author: the author of the book
        pages: total number of pages
    """

    def __init__(self, name: str, author: str, pages: int) -> None:
        self.name = name
        self.author = author
        self.pages = pages

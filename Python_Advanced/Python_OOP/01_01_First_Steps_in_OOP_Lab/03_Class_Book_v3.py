class Book:
    """
    Store book name, author, and pages.

    Args:
        name: title of the book
        author: name of the author
        pages: number of pages in the book
    """

    def __init__(self, name: str, author: str, pages: int) -> None:
        self.name = name
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f'"{self.name}" by {self.author}, {self.pages} pages'

    def __repr__(self) -> str:
        return f'Book(name={self.name!r}, author={self.author!r}, pages={self.pages})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return False
        return self.name == other.name and self.author == other.author and self.pages == other.pages

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages < other.pages

    def __len__(self) -> int:
        return self.pages

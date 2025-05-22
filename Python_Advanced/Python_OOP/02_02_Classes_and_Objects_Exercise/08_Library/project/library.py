class Library:
    """
    This class represents a library. It keeps track of users, available books, and rented books.
    """

    def __init__(self) -> None:
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: object) -> str:
        """
        This method allows a user to rent a book if it is available.

        Args:
            author (str): The author of the book
            book_name (str): The title of the book
            days_to_return (int): Number of days before returning
            user (User): The user renting the book

        Returns:
            str: A message about the action taken
        """
        if author in self.books_available and book_name in self.books_available[author]:
            self.books_available[author].remove(book_name)
            user.books.append(book_name)
            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}
            self.rented_books[user.username][book_name] = days_to_return
            return f'{book_name} successfully rented for the next {days_to_return} days!'

        for username, books in self.rented_books.items():
            if book_name in books:
                return f'The book "{book_name}" is already rented and will be available in {books[book_name]} days!'

        return f'The book "{book_name}" is not available in the library!'

    def return_book(self, author: str, book_name: str, user: object) -> str | None:
        """
        This method allows a user to return a book back to the library.

        Args:
            author (str): The author of the book
            book_name (str): The title of the book
            user (User): The user returning the book

        Returns:
            str | None: An error message or None if successful
        """
        if book_name in user.books:
            user.books.remove(book_name)
            if author not in self.books_available:
                self.books_available[author] = []
            self.books_available[author].append(book_name)

            if user.username in self.rented_books and book_name in self.rented_books[user.username]:
                del self.rented_books[user.username][book_name]
                if not self.rented_books[user.username]:
                    del self.rented_books[user.username]
        else:
            return f'{user.username} doesn\'t have this book in his/her records!'

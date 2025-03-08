class Article:
    def __init__(self, title: str, content: str, author: str):
        """Initializes the article with a title, content, and author."""
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_content: str):
        """Changes the article's content to the new one."""
        self.content = new_content

    def change_author(self, new_author: str):
        """Changes the article's author to the new one."""
        self.author = new_author

    def rename(self, new_title: str):
        """Changes the article's title to the new one."""
        self.title = new_title

    def __repr__(self) -> str:
        """Returns a formatted string representation of the article."""
        return f'{self.title} - {self.content}: {self.author}'

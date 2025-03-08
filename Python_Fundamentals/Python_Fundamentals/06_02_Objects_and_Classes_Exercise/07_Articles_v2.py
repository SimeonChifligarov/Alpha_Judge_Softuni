class Article:
    """
    Represents an article with a title, content, and author, allowing edits, renaming, and author changes.
    """

    def __init__(self, title: str, content: str, author: str) -> None:
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_content: str) -> None:
        self.content = new_content

    def change_author(self, new_author: str) -> None:
        self.author = new_author

    def rename(self, new_title: str) -> None:
        self.title = new_title

    def __repr__(self) -> str:
        return f'{self.title} - {self.content}: {self.author}'

# if __name__ == '__main__':
#     article_instance = Article(title=input(), content=input(), author=input())
#
#     article_instance.edit(new_content=input())
#     article_instance.change_author(new_author=input())
#     article_instance.rename(new_title=input())
#
#     print(article_instance)

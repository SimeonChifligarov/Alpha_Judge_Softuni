class Comment:
    """
    Represents a comment with a username, content, and likes.
    """

    def __init__(self, username: str, content: str, likes: int = 0) -> None:
        self.username = username
        self.content = content
        self.likes = likes


if __name__ == '__main__':
    comment_instance = Comment(username='JohnDoe', content='Great post!', likes=5)
    print(comment_instance.username, comment_instance.content, comment_instance.likes)

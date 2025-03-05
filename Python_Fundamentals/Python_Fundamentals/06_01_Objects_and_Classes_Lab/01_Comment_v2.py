from dataclasses import dataclass


@dataclass
class Comment:
    username: str
    content: str
    likes: int = 0

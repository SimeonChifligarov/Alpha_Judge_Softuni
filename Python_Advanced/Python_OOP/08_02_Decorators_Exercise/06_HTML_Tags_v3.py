from typing import Callable


class TagsDecorator:
    """
    This class wraps the result of a function inside given HTML tag.
    """

    def __init__(self, tag: str) -> None:
        self.tag = tag

    def __call__(self, function: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> str:
            return f'<{self.tag}>{function(*args, **kwargs)}</{self.tag}>'

        return wrapper

    def __str__(self) -> str:
        return f'TagsDecorator with tag {self.tag}'

    def __repr__(self) -> str:
        return f'TagsDecorator(tag={self.tag})'


def tags(tag: str) -> Callable[[Callable], Callable]:
    """
    This function applies TagsDecorator to a function.
    Args:
        tag (str): HTML tag to wrap with
    Returns:
        Callable: decorated function
    """
    return TagsDecorator(tag=tag)

# if __name__ == '__main__':
#     @tags(tag='p')
#     def join_strings(*args: str) -> str:
#         return ''.join(args)
#     output = join_strings('Hello', ' you!')
#     print(output)
#     @tags(tag='h1')
#     def to_upper(text: str) -> str:
#         return text.upper()
#     output = to_upper('hello')
#     print(output)
#     pass

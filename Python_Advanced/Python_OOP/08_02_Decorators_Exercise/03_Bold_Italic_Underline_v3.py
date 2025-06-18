from typing import Callable


class HTMLDecorator:
    """
    This class wraps the result of a function inside HTML tags.
    """

    def __init__(self, function: Callable, tag: str) -> None:
        self.function = function
        self.tag = tag

    def __call__(self, *args, **kwargs) -> str:
        return f'<{self.tag}>{self.function(*args, **kwargs)}</{self.tag}>'

    def __str__(self) -> str:
        return f'HTMLDecorator with tag {self.tag}'

    def __repr__(self) -> str:
        return f'HTMLDecorator(function={self.function.__name__}, tag={self.tag})'


def make_bold(function: Callable) -> Callable:
    """
    This function applies bold HTML tag to another function result.
    Args:
        function (Callable): function to decorate
    Returns:
        Callable: decorated function
    """
    return HTMLDecorator(function=function, tag='b')


def make_italic(function: Callable) -> Callable:
    """
    This function applies italic HTML tag to another function result.
    Args:
        function (Callable): function to decorate
    Returns:
        Callable: decorated function
    """
    return HTMLDecorator(function=function, tag='i')


def make_underline(function: Callable) -> Callable:
    """
    This function applies underline HTML tag to another function result.
    Args:
        function (Callable): function to decorate
    Returns:
        Callable: decorated function
    """
    return HTMLDecorator(function=function, tag='u')

# if __name__ == '__main__':
#     @make_bold
#     @make_italic
#     @make_underline
#     def greet(name: str) -> str:
#         return f'Hello, {name}'
#     output = greet(name='Peter')
#     print(output)
#     @make_bold
#     @make_italic
#     @make_underline
#     def greet_all(*args: str) -> str:
#         return f'Hello, {", ".join(args)}'
#     output = greet_all('Peter', 'George')
#     print(output)
#     pass

from typing import Callable


def make_bold(function: Callable) -> Callable:
    """
    This function wraps the result of another function in <b> tags.
    Args:
        function (Callable): function to decorate
    Returns:
        Callable: decorated function
    """

    def wrapper(*args, **kwargs) -> str:
        return f'<b>{function(*args, **kwargs)}</b>'

    return wrapper


def make_italic(function: Callable) -> Callable:
    """
    This function wraps the result of another function in <i> tags.
    Args:
        function (Callable): function to decorate
    Returns:
        Callable: decorated function
    """

    def wrapper(*args, **kwargs) -> str:
        return f'<i>{function(*args, **kwargs)}</i>'

    return wrapper


def make_underline(function: Callable) -> Callable:
    """
    This function wraps the result of another function in <u> tags.
    Args:
        function (Callable): function to decorate
    Returns:
        Callable: decorated function
    """

    def wrapper(*args, **kwargs) -> str:
        return f'<u>{function(*args, **kwargs)}</u>'

    return wrapper

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

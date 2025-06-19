from typing import Callable


def tags(tag: str) -> Callable[[Callable], Callable]:
    """
    This function wraps the result of another function inside given HTML tag.
    Args:
        tag (str): HTML tag to wrap with
    Returns:
        Callable: decorated function
    """

    def decorator(function: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> str:
            return f'<{tag}>{function(*args, **kwargs)}</{tag}>'

        return wrapper

    return decorator

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

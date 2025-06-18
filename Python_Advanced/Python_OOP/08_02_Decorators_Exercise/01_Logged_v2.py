from typing import Callable, Any


def logged(function: Callable) -> Callable:
    """
    This function logs the call and result of another function, and returns the log.
    Args:
        function (Callable): function to decorate
    Returns:
        Callable: decorated function returning a string
    """

    def wrapper(*args, **kwargs) -> str:
        args_str = ', '.join(str(arg) for arg in args)
        called_message = f'you called {function.__name__}({args_str})'
        result = function(*args, **kwargs)
        returned_message = f'it returned {result}'
        return f'{called_message}\n{returned_message}'

    return wrapper

# if __name__ == '__main__':
#     @logged
#     def func(*args: int) -> int:
#         return 3 + len(args)
#     output = func(4, 4, 4)
#     print(output)
#     @logged
#     def sum_func(a: int, b: int) -> int:
#         return a + b
#     output = sum_func(1, 4)
#     print(output)
#     pass

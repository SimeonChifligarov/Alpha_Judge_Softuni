from typing import Callable, Any


def even_parameters(function: Callable) -> Callable:
    """
    This function checks if all parameters are even numbers before calling.
    Args:
        function (Callable): function to decorate
    Returns:
        Callable: decorated function or error message
    """

    def wrapper(*args, **kwargs) -> Any:
        if not all(isinstance(arg, int) and arg % 2 == 0 for arg in args):
            return 'Please use only even numbers!'
        return function(*args, **kwargs)

    return wrapper

# if __name__ == '__main__':
#     @even_parameters
#     def add(a: int, b: int) -> int:
#         return a + b
#     output = add(2, 4)
#     print(output)
#     output = add('Peter', 1)
#     print(output)
#     @even_parameters
#     def multiply(*nums: int) -> int:
#         result = 1
#         for num in nums:
#             result *= num
#         return result
#     output = multiply(2, 4, 6, 8)
#     print(output)
#     output = multiply(2, 4, 9, 8)
#     print(output)
#     pass

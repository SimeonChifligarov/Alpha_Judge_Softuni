from typing import Callable, Any


class EvenParametersDecorator:
    """
    This class checks if all parameters are even numbers before calling.
    """

    def __init__(self, function: Callable) -> None:
        self.function = function

    def __call__(self, *args, **kwargs) -> Any:
        if not all(isinstance(arg, int) and arg % 2 == 0 for arg in args):
            return 'Please use only even numbers!'
        return self.function(*args, **kwargs)

    def __str__(self) -> str:
        return f'EvenParametersDecorator for {self.function.__name__}'

    def __repr__(self) -> str:
        return f'EvenParametersDecorator(function={self.function.__name__})'


def even_parameters(function: Callable) -> Callable:
    """
    This function applies EvenParametersDecorator to a function.
    Args:
        function (Callable): function to decorate
    Returns:
        Callable: decorated function or error message
    """
    return EvenParametersDecorator(function=function)

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

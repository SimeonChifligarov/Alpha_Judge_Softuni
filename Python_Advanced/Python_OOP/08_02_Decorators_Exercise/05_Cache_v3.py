from typing import Callable


class CacheDecorator:
    """
    This class caches the results of a function.
    """

    def __init__(self, function: Callable[[int], int]) -> None:
        self.function = function
        self.log = {}

    def __call__(self, n: int) -> int:
        if n not in self.log:
            self.log[n] = self.function(n)
        return self.log[n]

    def __str__(self) -> str:
        return f'CacheDecorator for {self.function.__name__}'

    def __repr__(self) -> str:
        return f'CacheDecorator(function={self.function.__name__})'


def cache(func: Callable[[int], int]) -> Callable[[int], int]:
    """
    This function applies CacheDecorator to a function.
    Args:
        func (Callable[[int], int]): function to cache
    Returns:
        Callable[[int], int]: decorated function
    """
    decorator_instance = CacheDecorator(function=func)
    decorator_instance.log = decorator_instance.log
    return decorator_instance

# if __name__ == '__main__':
#     @cache
#     def fibonacci(n: int) -> int:
#         if n < 2:
#             return n
#         else:
#             return fibonacci(n=n-1) + fibonacci(n=n-2)
#     fibonacci(n=3)
#     print(fibonacci.log)
#     fibonacci(n=4)
#     print(fibonacci.log)
#     pass

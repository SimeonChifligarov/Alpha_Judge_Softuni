from typing import Callable


def cache(func: Callable[[int], int]) -> Callable[[int], int]:
    """
    This function caches the results of the fibonacci function.
    Args:
        func (Callable[[int], int]): fibonacci function
    Returns:
        Callable[[int], int]: decorated function with caching
    """
    log_dict = {}

    def wrapper(n: int) -> int:
        if n not in log_dict:
            log_dict[n] = func(n)
        return log_dict[n]

    wrapper.log = log_dict
    return wrapper

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

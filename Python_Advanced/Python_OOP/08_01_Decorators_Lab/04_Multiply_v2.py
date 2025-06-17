from typing import Callable


def multiply(times: int) -> Callable[[Callable[[int], int]], Callable[[int], int]]:
    """
    This function multiplies the result of another function by times.
    Args:
        times (int): multiplier value
    Returns:
        Callable: decorator that multiplies function result
    """

    def decorator(function: Callable[[int], int]) -> Callable[[int], int]:
        def wrapper(number: int) -> int:
            return function(number) * times

        return wrapper

    return decorator

# if __name__ == '__main__':
#     @multiply(times=3)
#     def add_ten(number: int) -> int:
#         return number + 10
#     output = add_ten(number=3)
#     print(output)
#     @multiply(times=5)
#     def add_ten(number: int) -> int:
#         return number + 10
#     output = add_ten(number=6)
#     print(output)
#     pass

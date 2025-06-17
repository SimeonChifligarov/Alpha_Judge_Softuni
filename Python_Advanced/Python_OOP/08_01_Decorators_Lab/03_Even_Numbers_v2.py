from typing import Callable


def even_numbers(function: Callable[[list[int]], list[int]]) -> Callable[[list[int]], list[int]]:
    """
    This function keeps only even numbers from the result of another function.
    Args:
        function (Callable[[list[int]], list[int]]): function returning list of numbers
    Returns:
        Callable[[list[int]], list[int]]: new function returning only even numbers
    """

    def wrapper(numbers: list[int]) -> list[int]:
        return [number for number in function(numbers) if number % 2 == 0]

    return wrapper

# if __name__ == '__main__':
#     @even_numbers
#     def get_numbers(numbers: list[int]) -> list[int]:
#         return numbers
#     output = get_numbers(numbers=[1, 2, 3, 4, 5])
#     print(output)
#     pass

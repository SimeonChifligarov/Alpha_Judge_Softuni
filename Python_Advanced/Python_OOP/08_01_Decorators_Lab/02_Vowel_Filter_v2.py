from typing import Callable


def vowel_filter(function: Callable[[], list[str]]) -> Callable[[], list[str]]:
    """
    This function keeps only vowels from the result of another function.
    Args:
        function (Callable[[], list[str]]): function returning list of letters
    Returns:
        Callable[[], list[str]]: new function returning only vowels
    """

    def wrapper() -> list[str]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return [char for char in function() if char in vowels]

    return wrapper

# if __name__ == '__main__':
#     @vowel_filter
#     def get_letters() -> list[str]:
#         return ['a', 'b', 'c', 'd', 'e']
#     output = get_letters()
#     print(output)
#     pass

from typing import Iterator
from itertools import permutations


def possible_permutations(elements: list) -> Iterator[list]:
    """
    This function gives all possible permutations of the list.
    Args:
        elements (list): list of elements
    Yields:
        list: one permutation at a time
    """
    for perm in permutations(elements):
        yield list(perm)

# if __name__ == '__main__':
#     output = [print(item) for item in possible_permutations(elements=[1, 2, 3])]
#     output = [print(item) for item in possible_permutations(elements=[1])]
#     pass

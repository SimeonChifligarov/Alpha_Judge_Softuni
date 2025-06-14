from typing import Iterator


class PermutationsGenerator:
    """
    This class gives a generator for all permutations of a list.
    """

    def __init__(self) -> None:
        pass

    def __call__(self, elements: list) -> Iterator[list]:
        return self.possible_permutations(elements=elements)

    def __str__(self) -> str:
        return 'PermutationsGenerator for making permutations'

    def __repr__(self) -> str:
        return 'PermutationsGenerator()'

    def possible_permutations(self, elements: list) -> Iterator[list]:
        """
        This function gives all possible permutations of the list.
        Args:
            elements (list): list of elements
        Yields:
            list: one permutation at a time
        """
        if len(elements) <= 1:
            yield elements
        else:
            for index in range(len(elements)):
                picked = elements[index]
                remaining = elements[:index] + elements[index + 1:]
                for variant in self.possible_permutations(remaining):
                    yield [picked] + variant


possible_permutations = PermutationsGenerator().possible_permutations

# if __name__ == '__main__':
#     output = [print(item) for item in possible_permutations(elements=[1, 2, 3])]
#     output = [print(item) for item in possible_permutations(elements=[1])]
#     pass

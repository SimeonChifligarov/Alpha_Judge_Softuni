from typing import Iterator


class PrimeGenerator:
    """
    This class gives a generator for prime numbers.
    """

    def __init__(self) -> None:
        pass

    def __call__(self, numbers: list[int]) -> Iterator[int]:
        return self.get_primes(numbers=numbers)

    def __str__(self) -> str:
        return 'PrimeGenerator for extracting prime numbers'

    def __repr__(self) -> str:
        return 'PrimeGenerator()'

    def get_primes(self, numbers: list[int]) -> Iterator[int]:
        """
        This function gives only prime numbers from the input list.
        Args:
            numbers (list[int]): list of integers
        Yields:
            int: prime numbers from the list
        """
        for value in numbers:
            if value < 2:
                continue
            for divider in range(2, int(value ** 0.5) + 1):
                if value % divider == 0:
                    break
            else:
                yield value


get_primes = PrimeGenerator().get_primes

# if __name__ == '__main__':
#     output = list(get_primes(numbers=[2, 4, 3, 5, 6, 9, 1, 0]))
#     print(output)
#     output = list(get_primes(numbers=[-2, 0, 0, 1, 1, 0]))
#     print(output)
#     pass

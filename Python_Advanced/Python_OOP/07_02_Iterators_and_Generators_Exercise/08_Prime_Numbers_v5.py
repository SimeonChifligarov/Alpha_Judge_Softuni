from typing import Iterator


def get_primes(numbers: list[int]) -> Iterator[int]:
    """
    This function gives only prime numbers from the input list.
    Args:
        numbers (list[int]): list of integers
    Yields:
        int: prime numbers from the list
    """
    for number in numbers:
        if number < 2:
            continue
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                break
        else:
            yield number

# if __name__ == '__main__':
#     output = list(get_primes([2, 4, 3, 5, 6, 9, 1, 0]))
#     print(output)
#     output = list(get_primes([-2, 0, 0, 1, 1, 0]))
#     print(output)
#     pass

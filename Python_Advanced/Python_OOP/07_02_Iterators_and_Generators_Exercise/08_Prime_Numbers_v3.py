from typing import Iterator


def is_prime(number: int) -> bool:
    """
    This function checks if a number is prime.
    Args:
        number (int): number to check
    Returns:
        bool: True if prime, False otherwise
    """
    if number < 2:
        return False
    for divider in range(2, int(number ** 0.5) + 1):
        if number % divider == 0:
            return False
    return True


def get_primes(numbers: list[int]) -> Iterator[int]:
    """
    This function gives only prime numbers from the input list.
    Args:
        numbers (list[int]): list of integers
    Yields:
        int: prime numbers from the list
    """
    for value in numbers:
        if is_prime(number=value):
            yield value

# if __name__ == '__main__':
#     output = list(get_primes(numbers=[2, 4, 3, 5, 6, 9, 1, 0]))
#     print(output)
#     output = list(get_primes(numbers=[-2, 0, 0, 1, 1, 0]))
#     print(output)
#     pass

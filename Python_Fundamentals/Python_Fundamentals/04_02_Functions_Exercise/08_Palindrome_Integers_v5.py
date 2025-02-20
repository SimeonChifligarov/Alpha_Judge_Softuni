def check_palindromes(numbers: list[int]) -> list[bool]:
    """
    Returns a list of booleans indicating whether each number in the given list is a palindrome.
    """
    return [str(num) == str(num)[::-1] for num in numbers]


if __name__ == '__main__':
    input_numbers = [int(el) for el in input().split(', ')]
    results = check_palindromes(numbers=input_numbers)
    [print(r) for r in results]

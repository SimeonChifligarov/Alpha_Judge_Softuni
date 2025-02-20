def check_palindrome(number: int) -> bool:
    """
    Returns True if the given number is a palindrome, otherwise False.
    """
    return str(number) == str(number)[::-1]


if __name__ == '__main__':
    input_numbers = [int(el) for el in input().split(', ')]
    results = [check_palindrome(number=num) for num in input_numbers]
    [print(r) for r in results]

def check_palindrome(number: int) -> bool:
    """
    Returns True if the given number is a palindrome, otherwise False.
    """
    num_str = str(number)
    length = len(num_str)
    for i in range(length // 2):
        if num_str[i] != num_str[length - 1 - i]:
            return False
    return True


if __name__ == '__main__':
    input_numbers = [int(el) for el in input().split(', ')]
    results = [check_palindrome(number=num) for num in input_numbers]
    [print(r) for r in results]

def get_even_numbers(numbers: list[int]) -> list[int]:
    """
    Returns a list of even numbers from the given list using filter().
    """
    return list(filter(lambda num: num % 2 == 0, numbers))


if __name__ == '__main__':
    input_numbers = list(map(int, input().split()))
    result = get_even_numbers(numbers=input_numbers)
    print(result)

def sort_numbers(numbers: list[int]) -> list[int]:
    """
    Returns a sorted list of numbers in ascending order using sorted().
    """
    return sorted(numbers)


if __name__ == '__main__':
    input_numbers = [int(el) for el in input().split()]
    result = sort_numbers(numbers=input_numbers)
    print(result)

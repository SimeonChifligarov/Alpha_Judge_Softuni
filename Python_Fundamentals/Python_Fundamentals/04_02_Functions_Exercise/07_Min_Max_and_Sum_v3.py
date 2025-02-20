def calculate_min_max_sum(numbers: list[int]) -> tuple[int, int, int]:
    """
    Returns the minimum, maximum, and sum of the given list of numbers using min(), max(), and sum().
    """
    return min(numbers), max(numbers), sum(numbers)


if __name__ == '__main__':
    input_numbers = [int(el) for el in input().split()]
    min_result, max_result, sum_result = calculate_min_max_sum(numbers=input_numbers)
    print(f'The minimum number is {min_result}')
    print(f'The maximum number is {max_result}')
    print(f'The sum number is: {sum_result}')

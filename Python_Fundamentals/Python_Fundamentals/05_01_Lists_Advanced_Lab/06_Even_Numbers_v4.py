def find_even_indices(numbers: list[int]) -> list[int]:
    """
    Finds the indices of all even numbers in the given list.
    """
    return [index for index, number in enumerate(numbers) if number % 2 == 0]


if __name__ == '__main__':
    numbers_input = [int(num) for num in input().split(', ')]
    even_indices = find_even_indices(numbers=numbers_input)
    print(even_indices)

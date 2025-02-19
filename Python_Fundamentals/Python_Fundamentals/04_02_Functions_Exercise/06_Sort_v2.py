def sort_numbers(numbers: list[int]) -> list[int]:
    """
    Returns a sorted list of numbers in ascending order using bubble sort.
    """
    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


if __name__ == '__main__':
    # input_numbers = list(map(int, input().split()))
    input_numbers = [int(el) for el in input().split()]
    result = sort_numbers(numbers=input_numbers)
    print(result)

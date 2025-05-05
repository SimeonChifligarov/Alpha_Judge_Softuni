def recursive_sum(numbers: list[int], index: int = 0) -> int:
    """
    Get the sum of all numbers in the list using recursion.

    Args:
        numbers: list of integers
        index: current index for recursion

    Returns:
        The total sum of the list
    """
    if index == len(numbers):
        return 0
    return numbers[index] + recursive_sum(numbers=numbers, index=index + 1)


if __name__ == '__main__':
    input_numbers = [int(el) for el in input().split()]
    total_sum = recursive_sum(numbers=input_numbers)
    print(total_sum)

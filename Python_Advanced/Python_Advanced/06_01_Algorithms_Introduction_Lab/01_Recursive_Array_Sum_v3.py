def recursive_sum(numbers: list[int], index: int = 0) -> int:
    """
    Calculate the total of a list using recursion.

    Args:
        numbers: list of integers
        index: position in the list

    Returns:
        Sum of integers
    """
    return 0 if index == len(numbers) else numbers[index] + recursive_sum(numbers=numbers, index=index + 1)


if __name__ == '__main__':
    input_numbers = [int(el) for el in input().split()]
    total_sum = recursive_sum(numbers=input_numbers)
    print(total_sum)

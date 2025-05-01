def separate_and_compare(numbers: list[int]) -> None:
    """
    This function takes a list of numbers and separates them into positives and negatives.
    Then it sums them up and prints the results.

    Args:
        numbers: A list of integers

    Returns:
        None
    """
    negatives = [n for n in numbers if n < 0]
    positives = [n for n in numbers if n > 0]
    sum_negatives = sum(negatives)
    sum_positives = sum(positives)
    print(sum_negatives)
    print(sum_positives)
    if abs(sum_negatives) > sum_positives:
        print('The negatives are stronger than the positives')
    else:
        print('The positives are stronger than the negatives')


if __name__ == '__main__':
    input_numbers = [int(value) for value in input().split()]
    separate_and_compare(numbers=input_numbers)

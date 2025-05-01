def analyze_numbers(values: list[int]) -> None:
    """
    This function takes numbers, finds the sums of negatives and positives,
    and then prints the sums and who is stronger.

    Args:
        values: A list of integers

    Returns:
        None
    """
    sum_negatives = sum([el for el in values if el < 0])
    sum_positives = sum([el for el in values if el > 0])
    results = [sum_negatives, sum_positives]
    [print(result) for result in results]
    print('The negatives are stronger than the positives' if abs(
        sum_negatives) > sum_positives else 'The positives are stronger than the negatives')


if __name__ == '__main__':
    given_values = [int(element) for element in input().split()]
    analyze_numbers(values=given_values)

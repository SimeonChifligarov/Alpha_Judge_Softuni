def process_numbers(elements: list[int]) -> None:
    """
    This function separates numbers into positives and negatives,
    calculates their sums, and shows who is stronger.

    Args:
        elements: A list of integers

    Returns:
        None
    """
    sum_negatives = sum(filter(lambda x: x < 0, elements))
    sum_positives = sum(filter(lambda x: x > 0, elements))

    message = 'The negatives are stronger than the positives' if abs(
        sum_negatives) > sum_positives else 'The positives are stronger than the negatives'
    
    print(sum_negatives)
    print(sum_positives)
    print(message)


if __name__ == '__main__':
    input_elements = [int(item) for item in input().split()]
    process_numbers(elements=input_elements)

def categorize_numbers(numbers: list[int]) -> tuple[list[int], list[int], list[int], list[int]]:
    """
    Categorizes numbers into positive, negative, even, and odd.

    :param numbers: List of integers.
    :return: Tuple containing four lists: positive, negative, even, and odd numbers.
    """
    positives, negatives, evens, odds = [], [], [], []

    for num in numbers:
        (positives if num >= 0 else negatives).append(num)
        (evens if num % 2 == 0 else odds).append(num)

    return positives, negatives, evens, odds


if __name__ == '__main__':
    input_numbers = [int(el) for el in input().split(', ')]
    pos, neg, even, odd = categorize_numbers(numbers=input_numbers)

    print(f'Positive: {", ".join(map(str, pos))}')
    print(f'Negative: {", ".join(map(str, neg))}')
    print(f'Even: {", ".join(map(str, even))}')
    print(f'Odd: {", ".join(map(str, odd))}')

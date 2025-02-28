def categorize_numbers(numbers: list[int]) -> tuple[list[int], list[int], list[int], list[int]]:
    """
    Categorizes numbers into positive, negative, even, and odd.

    :param numbers: List of integers.
    :return: Tuple containing four lists: positive, negative, even, and odd numbers.
    """
    positives = [num for num in numbers if num >= 0]
    negatives = [num for num in numbers if num < 0]
    evens = [num for num in numbers if num % 2 == 0]
    odds = [num for num in numbers if num % 2 != 0]

    return positives, negatives, evens, odds


if __name__ == '__main__':
    input_numbers = [int(el) for el in input().split(', ')]
    pos, neg, even, odd = categorize_numbers(numbers=input_numbers)

    print(f'Positive: {", ".join([str(el) for el in pos])}')
    print(f'Negative: {", ".join([str(el) for el in neg])}')
    print(f'Even: {", ".join([str(el) for el in even])}')
    print(f'Odd: {", ".join([str(el) for el in odd])}')

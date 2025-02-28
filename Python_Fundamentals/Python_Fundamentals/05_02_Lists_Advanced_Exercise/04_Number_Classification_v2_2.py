if __name__ == '__main__':
    numbers = [int(el) for el in input().split(', ')]

    positives = [num for num in numbers if num >= 0]
    negatives = [num for num in numbers if num < 0]
    evens = [num for num in numbers if num % 2 == 0]
    odds = [num for num in numbers if num % 2 != 0]

    print(f'Positive: {", ".join(map(str, positives))}')
    print(f'Negative: {", ".join(map(str, negatives))}')
    print(f'Even: {", ".join(map(str, evens))}')
    print(f'Odd: {", ".join(map(str, odds))}')

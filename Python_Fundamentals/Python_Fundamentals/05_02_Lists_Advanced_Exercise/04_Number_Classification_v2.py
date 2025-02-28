if __name__ == '__main__':
    numbers = [int(el) for el in input().split(', ')]

    positives, negatives, evens, odds = [], [], [], []

    for num in numbers:
        if num >= 0:
            positives.append(num)
        else:
            negatives.append(num)

        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    print(f'Positive: {", ".join([str(el) for el in positives])}')
    print(f'Negative: {", ".join([str(el) for el in negatives])}')
    print(f'Even: {", ".join([str(el) for el in evens])}')
    print(f'Odd: {", ".join([str(el) for el in odds])}')

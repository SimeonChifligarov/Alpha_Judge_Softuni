from typing import List, Tuple


def separate_numbers(count: int) -> Tuple[List[int], List[int]]:
    positives = []
    negatives = []
    for _ in range(count):
        number = int(input())
        if number >= 0:
            positives.append(number)
        else:
            negatives.append(number)

    return positives, negatives


if __name__ == '__main__':
    count_input = int(input())
    positives_nums, negatives_nums = separate_numbers(count=count_input)
    print(positives_nums)
    print(negatives_nums)
    print(f'Count of positives: {len(positives_nums)}')
    print(f'Sum of negatives: {sum(negatives_nums)}')

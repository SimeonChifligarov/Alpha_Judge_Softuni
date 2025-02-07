from typing import List


def filter_numbers(count: int) -> List[int]:
    numbers = [int(input()) for _ in range(count)]
    category = input()
    if category == 'even':
        return [num for num in numbers if num % 2 == 0]
    elif category == 'odd':
        return [num for num in numbers if num % 2 != 0]
    elif category == 'negative':
        return [num for num in numbers if num < 0]
    elif category == 'positive':
        return [num for num in numbers if num >= 0]


if __name__ == '__main__':
    count_input = int(input())
    result = filter_numbers(count=count_input)
    print(result)

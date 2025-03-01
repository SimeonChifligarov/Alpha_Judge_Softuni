def group_numbers(numbers: list[int]) -> None:
    max_group = (
        max(numbers) + 10 if max(numbers) % 10 != 0
        else max(numbers)
    )

    for group in range(10, max_group + 1, 10):
        grouped_numbers = [num for num in numbers if num <= group]
        numbers = [num for num in numbers if num > group]

        print(f'Group of {group}\'s: {grouped_numbers}')


if __name__ == '__main__':
    numbers_list = [int(num) for num in input().split(', ')]
    group_numbers(numbers=numbers_list)

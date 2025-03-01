def group_numbers(numbers: list[int]) -> None:
    max_group = (
        max(numbers) + 10 if max(numbers) % 10 != 0
        else max(numbers)
    )

    grouped_data = {}

    for group in range(10, max_group + 1, 10):
        grouped_data[group] = []
        for num in numbers[:]:  # Iterate over a copy to modify the original list
            if num <= group:
                grouped_data[group].append(num)
                numbers.remove(num)

        print(f'Group of {group}\'s: {grouped_data[group]}')


if __name__ == '__main__':
    numbers_list = [int(num) for num in input().split(', ')]
    grouped_result = group_numbers(numbers=numbers_list)

def climbers_statistics_with_dict(groups_count, group_sizes):
    categories = {
        'Musala': 0,
        'Montblanc': 0,
        'Kilimanjaro': 0,
        'K2': 0,
        'Everest': 0
    }

    total_climbers = sum(group_sizes)

    for size in group_sizes:
        if size <= 5:
            categories['Musala'] += size
        elif 6 <= size <= 12:
            categories['Montblanc'] += size
        elif 13 <= size <= 25:
            categories['Kilimanjaro'] += size
        elif 26 <= size <= 40:
            categories['K2'] += size
        else:
            categories['Everest'] += size

    return '\n'.join(
        f'{(count / total_climbers) * 100:.2f}%' for count in categories.values()
    )


if __name__ == '__main__':
    groups_count_input = int(input())
    group_sizes_input = [int(input()) for _ in range(groups_count_input)]
    result = climbers_statistics_with_dict(groups_count=groups_count_input, group_sizes=group_sizes_input)
    print(result)

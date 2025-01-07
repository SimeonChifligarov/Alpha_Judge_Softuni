def climbers_statistics(groups_count, group_sizes):
    musala = 0
    montblanc = 0
    kilimanjaro = 0
    k2 = 0
    everest = 0

    total_climbers = sum(group_sizes)

    for size in group_sizes:
        if size <= 5:
            musala += size
        elif 6 <= size <= 12:
            montblanc += size
        elif 13 <= size <= 25:
            kilimanjaro += size
        elif 26 <= size <= 40:
            k2 += size
        else:
            everest += size

    return (
        f'{(musala / total_climbers) * 100:.2f}%',
        f'{(montblanc / total_climbers) * 100:.2f}%',
        f'{(kilimanjaro / total_climbers) * 100:.2f}%',
        f'{(k2 / total_climbers) * 100:.2f}%',
        f'{(everest / total_climbers) * 100:.2f}%',
    )


if __name__ == '__main__':
    groups_count_input = int(input())
    group_sizes_input = [int(input()) for _ in range(groups_count_input)]
    result = climbers_statistics(groups_count=groups_count_input, group_sizes=group_sizes_input)
    print('\n'.join(result))

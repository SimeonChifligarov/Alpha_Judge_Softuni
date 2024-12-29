def count_eggs_and_find_max(total_eggs):
    red_eggs = 0
    orange_eggs = 0
    blue_eggs = 0
    green_eggs = 0

    for _ in range(total_eggs):
        color = input()
        if color == 'red':
            red_eggs += 1
        elif color == 'orange':
            orange_eggs += 1
        elif color == 'blue':
            blue_eggs += 1
        elif color == 'green':
            green_eggs += 1

    egg_counts = {
        'red': red_eggs,
        'orange': orange_eggs,
        'blue': blue_eggs,
        'green': green_eggs,
    }
    max_color = max(egg_counts, key=egg_counts.get)
    max_count = egg_counts[max_color]

    print(f'Red eggs: {red_eggs}')
    print(f'Orange eggs: {orange_eggs}')
    print(f'Blue eggs: {blue_eggs}')
    print(f'Green eggs: {green_eggs}')
    print(f'Max eggs: {max_count} -> {max_color}')


total_eggs_input = int(input())
count_eggs_and_find_max(total_eggs_input)

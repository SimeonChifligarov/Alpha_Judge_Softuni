def process_input() -> dict[tuple[str, str], int]:
    dwarfs = {}

    while True:
        data = input()
        if data == 'Once upon a time':
            break

        name, hat_color, physics = data.split(' <:> ', maxsplit=2)
        physics = int(physics)

        if (name, hat_color) not in dwarfs or dwarfs[(name, hat_color)] < physics:
            dwarfs[(name, hat_color)] = physics

    return dwarfs


def print_results(dwarfs: dict[tuple[str, str], int]) -> None:
    hat_color_counts = {}
    for (_, hat_color) in dwarfs:
        hat_color_counts[hat_color] = hat_color_counts.get(hat_color, 0) + 1

    sorted_dwarfs = sorted(
        dwarfs.items(),
        key=lambda x: (-x[1], -hat_color_counts[x[0][1]])
    )

    for (name, hat_color), physics in sorted_dwarfs:
        print(f'({hat_color}) {name} <-> {physics}')


if __name__ == '__main__':
    dwarfs_data = process_input()
    print_results(dwarfs=dwarfs_data)

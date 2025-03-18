from collections import defaultdict


def process_dwarfs():
    dwarfs = {}
    hat_colors_count = defaultdict(int)

    while True:
        command = input()
        if command == 'Once upon a time':
            break

        name, hat_color, physics = command.split(' <:> ', maxsplit=2)
        physics = int(physics)

        if (name, hat_color) in dwarfs:
            if dwarfs[(name, hat_color)] < physics:
                dwarfs[(name, hat_color)] = physics
        else:
            dwarfs[(name, hat_color)] = physics
            hat_colors_count[hat_color] += 1

    sorted_dwarfs = sorted(dwarfs.items(), key=lambda x: (-x[1], -hat_colors_count[x[0][1]]))

    for (name, hat_color), physics in sorted_dwarfs:
        print(f'({hat_color}) {name} <-> {physics}')


if __name__ == '__main__':
    process_dwarfs()

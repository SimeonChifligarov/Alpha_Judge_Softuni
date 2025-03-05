def count_destroyed_ships(field: list[list[int]], attacks: str) -> int:
    """
    Counts the number of ships destroyed after attacks.

    :param field: 2D list representing the field with ship health values
    :param attacks: String of attacked coordinates in "row-col row-col" format
    :return: Number of destroyed ships
    """
    attack_positions = [tuple(map(int, pos.split('-'))) for pos in attacks.split()]
    destroyed_ships = 0

    for r, c in attack_positions:
        if field[r][c] > 0:
            field[r][c] -= 1
            if field[r][c] == 0:
                destroyed_ships += 1

    return destroyed_ships


if __name__ == '__main__':
    n_input = int(input())
    field_input = [[int(num) for num in input().split()] for _ in range(n_input)]
    attacks_input = input()

    result = count_destroyed_ships(field=field_input, attacks=attacks_input)
    print(result)

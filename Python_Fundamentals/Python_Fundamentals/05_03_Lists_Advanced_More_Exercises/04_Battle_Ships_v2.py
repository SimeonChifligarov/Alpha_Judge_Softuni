def count_destroyed_ships(n: int, field_data: list[str], attacks: str) -> int:
    """
    Counts the number of ships destroyed after attacks.

    :param n: Number of rows in the field
    :param field_data: List of strings representing field rows with numbers
    :param attacks: String of attacked coordinates in "row-col row-col" format
    :return: Number of destroyed ships
    """
    grid = [[int(num) for num in row.split()] for row in field_data]
    attack_positions = [tuple(map(int, pos.split('-'))) for pos in attacks.split()]

    destroyed_ships = 0

    for r, c in attack_positions:
        if grid[r][c] > 0:
            grid[r][c] -= 1
            if grid[r][c] == 0:
                destroyed_ships += 1

    return destroyed_ships


if __name__ == '__main__':
    n_input = int(input())
    field_input = [input() for _ in range(n_input)]
    attacks_input = input()

    result = count_destroyed_ships(n=n_input, field_data=field_input, attacks=attacks_input)
    print(result)

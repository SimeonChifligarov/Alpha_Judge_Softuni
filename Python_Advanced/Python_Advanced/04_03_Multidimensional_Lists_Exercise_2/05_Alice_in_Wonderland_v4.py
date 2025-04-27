def move_alice(position: tuple[int, int], direction: str) -> tuple[int, int]:
    """
    This function calculates Alice's next position based on the direction.

    Args:
    position: current position (row, col)
    direction: direction to move in ('up', 'down', 'left', 'right')

    Returns:
    The new position (row, col)
    """
    row, col = position
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }
    dr, dc = directions[direction]
    return row + dr, col + dc


if __name__ == '__main__':
    size = int(input())

    field = []
    alice_position = (0, 0)

    for i in range(size):
        row = input().split()
        field.append(row)
        if 'A' in row:
            alice_position = (i, row.index('A'))

    tea_collected = 0
    field[alice_position[0]][alice_position[1]] = '*'

    while tea_collected < 10:
        command = input()
        next_row, next_col = move_alice(position=alice_position, direction=command)

        if not (0 <= next_row < size and 0 <= next_col < size):
            print('Alice didn\'t make it to the tea party.')
            break

        cell = field[next_row][next_col]

        if cell == 'R':
            field[next_row][next_col] = '*'
            print('Alice didn\'t make it to the tea party.')
            break

        if cell.isdigit():
            tea_collected += int(cell)

        field[next_row][next_col] = '*'
        alice_position = (next_row, next_col)

    else:
        print('She did it! She went to the party.')

    for row in field:
        print(' '.join(row))

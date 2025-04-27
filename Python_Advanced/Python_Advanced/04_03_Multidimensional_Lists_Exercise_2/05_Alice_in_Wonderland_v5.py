def move_alice(position: tuple[int, int], direction: str) -> tuple[int, int]:
    """
    This function calculates Alice's next position based on the direction.

    Args:
    position: current position (row, col)
    direction: direction to move in ('up', 'down', 'left', 'right')

    Returns:
    The new position (row, col)
    """
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    dr, dc = directions[direction]
    return position[0] + dr, position[1] + dc


if __name__ == '__main__':
    size = int(input())
    field = [input().split() for _ in range(size)]
    row, col = next((r, c) for r in range(size) for c in range(size) if field[r][c] == 'A')

    tea = 0
    field[row][col] = '*'

    while tea < 10:
        command = input()
        row, col = move_alice((row, col), command)

        if not (0 <= row < size and 0 <= col < size) or field[row][col] == 'R':
            if 0 <= row < size and 0 <= col < size:
                field[row][col] = '*'
            print('Alice didn\'t make it to the tea party.')
            break

        if field[row][col].isdigit():
            tea += int(field[row][col])

        field[row][col] = '*'

    else:
        print('She did it! She went to the party.')

    [print(' '.join(r)) for r in field]

def move_miner(field_size: int, move_commands: list[str], field_map: list[list[str]]) -> str:
    """
    This function moves the miner through the field, collecting coal or ending the game.

    Args:
    field_size: the size of the square field
    move_commands: list of movement directions
    field_map: the full game field with start, coal, and end positions

    Returns:
    A message indicating the outcome and final miner position
    """
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

    total_coal = sum(row.count('c') for row in field_map)
    miner_pos = [(r, c) for r in range(field_size) for c in range(field_size) if field_map[r][c] == 's'][0]

    for move in move_commands:
        dr, dc = directions[move]
        nr, nc = miner_pos[0] + dr, miner_pos[1] + dc

        if not (0 <= nr < field_size and 0 <= nc < field_size):
            continue

        miner_pos = (nr, nc)
        cell = field_map[nr][nc]

        if cell == 'e':
            return f'Game over! ({nr}, {nc})'
        if cell == 'c':
            total_coal -= 1
            field_map[nr][nc] = '*'
            if total_coal == 0:
                return f'You collected all coal! ({nr}, {nc})'

    return f'{total_coal} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})'


if __name__ == '__main__':
    size = int(input())
    moves = input().split()
    field = [input().split() for _ in range(size)]

    result = move_miner(field_size=size, move_commands=moves, field_map=field)
    print(result)

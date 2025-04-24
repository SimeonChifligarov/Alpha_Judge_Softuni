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
    direction_moves = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }

    total_coal = 0
    miner_row = 0
    miner_col = 0

    for row in range(field_size):
        for col in range(field_size):
            if field_map[row][col] == 's':
                miner_row, miner_col = row, col
            if field_map[row][col] == 'c':
                total_coal += 1

    for command in move_commands:
        row_change, col_change = direction_moves[command]
        next_row = miner_row + row_change
        next_col = miner_col + col_change

        if 0 <= next_row < field_size and 0 <= next_col < field_size:
            miner_row, miner_col = next_row, next_col
            cell_value = field_map[miner_row][miner_col]

            if cell_value == 'e':
                return f'Game over! ({miner_row}, {miner_col})'
            elif cell_value == 'c':
                total_coal -= 1
                field_map[miner_row][miner_col] = '*'
                if total_coal == 0:
                    return f'You collected all coal! ({miner_row}, {miner_col})'

    return f'{total_coal} pieces of coal left. ({miner_row}, {miner_col})'


if __name__ == '__main__':
    field_size_input = int(input())
    commands_input = input().split()

    game_field = []
    for _ in range(field_size_input):
        row_data = input().split()
        game_field.append(row_data)

    result_message = move_miner(field_size=field_size_input, move_commands=commands_input, field_map=game_field)
    print(result_message)

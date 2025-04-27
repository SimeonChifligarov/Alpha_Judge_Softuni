from typing import List, Tuple


def is_inside(x: int, y: int, grid: List[List[str]]) -> bool:
    """
    Checks if a position is inside the grid.

    Args:
        x: Row
        y: Column
        grid: The field

    Returns:
        True if inside
    """
    return 0 <= x < len(grid) and 0 <= y < len(grid[x])


def run_training(field: List[List[str]], commands: List[str]) -> Tuple[str, List[List[int]]]:
    """
    Simulates shooting range with move and shoot commands.

    Args:
        field: The 5x5 grid
        commands: All move/shoot commands

    Returns:
        Result and list of shot targets
    """
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    my_pos = (-1, -1)
    hits, hit_count, targets = [], 0, 0

    for r in range(5):
        for c in range(5):
            if field[r][c] == 'A':
                my_pos = (r, c)
            if field[r][c] == 'x':
                targets += 1

    for command in commands:
        if hit_count == targets:
            break
        parts = command.split()
        act, dir = parts[0], parts[1]
        dx, dy = directions[dir]

        if act == 'move':
            steps = int(parts[2])
            nx, ny = my_pos[0] + dx * steps, my_pos[1] + dy * steps
            if is_inside(nx, ny, field) and field[nx][ny] == '.':
                field[my_pos[0]][my_pos[1]], my_pos = '.', (nx, ny)
                field[my_pos[0]][my_pos[1]] = 'A'

        elif act == 'shoot':
            for i in range(1, 6):
                sx, sy = my_pos[0] + dx * i, my_pos[1] + dy * i
                if not is_inside(sx, sy, field):
                    break
                if field[sx][sy] == 'x':
                    field[sx][sy], hit_count = '.', hit_count + 1
                    hits.append([sx, sy])
                    break

    return (
        f'Training completed! All {hit_count} targets hit.' if hit_count == targets
        else f'Training not completed! {targets - hit_count} targets left.',
        hits)


if __name__ == '__main__':
    grid_input = [input().split() for _ in range(5)]
    command_total = int(input())
    command_input = [input() for _ in range(command_total)]
    result_message, hit_list = run_training(field=grid_input, commands=command_input)
    print(result_message)
    [print(h) for h in hit_list]

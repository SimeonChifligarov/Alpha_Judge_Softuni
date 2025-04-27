def deliver_presents(presents: int, size: int, area: list[list[str]], commands: list[str]) -> None:
    """
    Move Santa in the grid and give presents. Ends when out of gifts or stopped.

    Args:
        presents: how many presents Santa has
        size: size of square grid
        area: grid of the neighborhood
        commands: list of directions

    Returns:
        None
    """

    def find_santa(grid: list[list[str]]) -> tuple[int, int]:
        return next((r, c) for r in range(size) for c in range(size) if grid[r][c] == 'S')

    def deliver_to_neighbors(r: int, c: int, count: int) -> int:
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if area[nr][nc] in {'V', 'X'} and count > 0:
                if area[nr][nc] == 'V':
                    received_kids[0] += 1
                area[nr][nc] = '-'
                count -= 1
        return count

    received_kids = [0]
    total_nice_kids = sum(row.count('V') for row in area)
    row_santa, col_santa = find_santa(area)
    movement = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

    for command in commands:
        if command == 'Christmas morning':
            break
        area[row_santa][col_santa] = '-'
        row_santa += movement[command][0]
        col_santa += movement[command][1]
        cell = area[row_santa][col_santa]
        if cell == 'V':
            received_kids[0] += 1
            presents -= 1
        elif cell == 'C':
            presents = deliver_to_neighbors(row_santa, col_santa, presents)
        area[row_santa][col_santa] = 'S'
        if presents == 0:
            break

    if presents == 0 and received_kids[0] < total_nice_kids:
        print('Santa ran out of presents!')
    [print(' '.join(row)) for row in area]
    print(f'Good job, Santa! {total_nice_kids} happy nice kid/s.' if received_kids[0] == total_nice_kids
          else f'No presents for {total_nice_kids - received_kids[0]} nice kid/s.')


if __name__ == '__main__':
    number_presents = int(input())
    matrix_size = int(input())
    neighborhood = [input().split() for _ in range(matrix_size)]

    directions = []
    try:
        while True:
            direction = input()
            directions.append(direction)
            if direction == 'Christmas morning':
                break
    except EOFError:
        pass

    deliver_presents(presents=number_presents, size=matrix_size, area=neighborhood, commands=directions)

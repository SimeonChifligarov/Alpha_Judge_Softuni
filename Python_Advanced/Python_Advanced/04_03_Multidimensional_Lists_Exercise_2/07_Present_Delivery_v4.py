def deliver_presents(presents: int, size: int, area: list[list[str]], commands: list[str]) -> None:
    """
    Move Santa in the grid and deliver presents to nice kids. Stop when out of presents or on command.

    Args:
        presents: number of presents Santa starts with
        size: size of the square matrix
        area: the neighborhood matrix
        commands: list of movement directions

    Returns:
        None
    """

    def find_santa(grid: list[list[str]]) -> tuple[int, int]:
        for row_index in range(size):
            for col_index in range(size):
                if grid[row_index][col_index] == 'S':
                    return row_index, col_index
        return -1, -1

    def deliver_to_neighbors(r: int, c: int, count: int) -> int:
        for row_shift, col_shift in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_r = r + row_shift
            new_c = c + col_shift
            if area[new_r][new_c] in {'V', 'X'} and count > 0:
                if area[new_r][new_c] == 'V':
                    received_kids[0] += 1
                area[new_r][new_c] = '-'
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
        current_cell = area[row_santa][col_santa]

        if current_cell == 'V':
            received_kids[0] += 1
            presents -= 1
        elif current_cell == 'C':
            presents = deliver_to_neighbors(row_santa, col_santa, presents)
        area[row_santa][col_santa] = 'S'

        if presents == 0:
            break

    if presents == 0 and received_kids[0] < total_nice_kids:
        print('Santa ran out of presents!')

    for line in area:
        print(' '.join(line))

    if received_kids[0] == total_nice_kids:
        print(f'Good job, Santa! {total_nice_kids} happy nice kid/s.')
    else:
        print(f'No presents for {total_nice_kids - received_kids[0]} nice kid/s.')


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

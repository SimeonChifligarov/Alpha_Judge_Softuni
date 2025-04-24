def detonate_bombs(matrix_size: int, matrix_data: list[list[int]], bomb_coords: list[tuple[int, int]]) -> None:
    """
    This function applies explosions from bombs to the matrix.

    Args:
    matrix_size: size of the square matrix
    matrix_data: the matrix of integers
    bomb_coords: list of coordinates where bombs are located

    Returns:
    Nothing, the matrix is updated in place
    """
    for row, col in bomb_coords:
        if matrix_data[row][col] <= 0:
            continue

        bomb_power = matrix_data[row][col]

        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if 0 <= r < matrix_size and 0 <= c < matrix_size and (r != row or c != col):
                    if matrix_data[r][c] > 0:
                        matrix_data[r][c] -= bomb_power

        matrix_data[row][col] = 0


def get_alive_cells(matrix_data: list[list[int]]) -> tuple[int, int]:
    """
    This function counts and sums the alive cells in the matrix.

    Args:
    matrix_data: the matrix with integers

    Returns:
    The count and the sum of all positive (alive) cells
    """
    alive_values = [cell for row in matrix_data for cell in row if cell > 0]
    return len(alive_values), sum(alive_values)


if __name__ == '__main__':
    matrix_size_input = int(input())

    matrix = []
    for _ in range(matrix_size_input):
        row_data = [int(x) for x in input().split()]
        matrix.append(row_data)

    raw_coords = input().split()
    bomb_positions = [(int(coord.split(',')[0]), int(coord.split(',')[1])) for coord in raw_coords]

    detonate_bombs(matrix_size=matrix_size_input, matrix_data=matrix, bomb_coords=bomb_positions)

    alive_count, alive_sum = get_alive_cells(matrix_data=matrix)

    print(f'Alive cells: {alive_count}')
    print(f'Sum: {alive_sum}')
    for cr in matrix:
        print(' '.join(str(cell) for cell in cr))

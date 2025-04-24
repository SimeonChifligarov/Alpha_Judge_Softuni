def detonate_bombs(matrix_size: int, matrix_data: list[list[int]], bomb_coords: list[tuple[int, int]]) -> None:
    """
    This function explodes all bombs, reducing values around them.

    Args:
    matrix_size: how many rows/columns the square matrix has
    matrix_data: the matrix of integers
    bomb_coords: list of coordinates for the bombs

    Returns:
    Nothing; matrix is modified directly
    """
    for row, col in bomb_coords:
        power = matrix_data[row][col]
        if power <= 0:
            continue
        for r in range(max(0, row - 1), min(matrix_size, row + 2)):
            for c in range(max(0, col - 1), min(matrix_size, col + 2)):
                if (r, c) != (row, col) and matrix_data[r][c] > 0:
                    matrix_data[r][c] -= power
        matrix_data[row][col] = 0


def get_alive_cells(matrix_data: list[list[int]]) -> tuple[int, int]:
    """
    This function counts how many cells are still alive and sums them.

    Args:
    matrix_data: the matrix after all explosions

    Returns:
    A tuple with count of alive cells and their total sum
    """
    alive = [val for row in matrix_data for val in row if val > 0]
    return len(alive), sum(alive)


if __name__ == '__main__':
    size = int(input())
    matrix = [[int(x) for x in input().split()] for _ in range(size)]
    bombs = [(int(x.split(',')[0]), int(x.split(',')[1])) for x in input().split()]

    detonate_bombs(matrix_size=size, matrix_data=matrix, bomb_coords=bombs)
    alive_count, alive_sum = get_alive_cells(matrix_data=matrix)

    print(f'Alive cells: {alive_count}')
    print(f'Sum: {alive_sum}')
    [print(' '.join(str(x) for x in row)) for row in matrix]

def largest_connected_dots(board: list[list[str]]) -> int:
    """
    Finds the largest count of connected dots in the board.

    :param board: 2D list representing the board with dots ('.') and dashes ('-')
    :return: Largest count of connected dots
    """

    def dfs(r: int, c: int) -> int:
        if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != '.' or visited[r][c]:
            return 0
        visited[r][c] = True
        return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

    rows, cols = len(board), len(board[0])
    visited = [[False] * cols for _ in range(rows)]
    max_dots = 0

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == '.' and not visited[row][col]:
                max_dots = max(max_dots, dfs(r=row, c=col))

    return max_dots


if __name__ == '__main__':
    n_input = int(input())
    board_input = [input().split() for _ in range(n_input)]

    result = largest_connected_dots(board=board_input)
    print(result)

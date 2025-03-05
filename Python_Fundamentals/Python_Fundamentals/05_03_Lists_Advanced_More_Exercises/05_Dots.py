def largest_connected_dots():
    def bfs(start_row, start_col):
        from collections import deque

        queue = deque([(start_row, start_col)])
        visited.add((start_row, start_col))
        count = 1

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and board[nr][nc] == '.':
                    visited.add((nr, nc))
                    queue.append((nr, nc))
                    count += 1

        return count

    n = int(input().strip())

    board = [input().strip().split() for _ in range(n)]

    rows, cols = n, len(board[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = set()
    max_dots = 0

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == '.' and (row, col) not in visited:
                max_dots = max(max_dots, bfs(start_row=row, start_col=col))

    print(max_dots)


if __name__ == '__main__':
    largest_connected_dots()

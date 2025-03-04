from collections import deque


def read_maze():
    n = int(input())
    maze = [list(input()) for _ in range(n)]
    return maze


def find_kate(maze):
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            if maze[r][c] == 'k':
                return r, c
    return None


def is_exit(maze, r, c):
    return r == 0 or c == 0 or r == len(maze) - 1 or c == len(maze[r]) - 1


def get_longest_escape(maze):
    start = find_kate(maze)
    if not start:
        return 'Kate cannot get out'

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add(start)
    max_moves = -1

    while queue:
        r, c, moves = queue.popleft()

        if is_exit(maze, r, c):
            max_moves = max(max_moves, moves)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(maze) and 0 <= nc < len(maze[nr]) and maze[nr][nc] == ' ' and (nr, nc) not in visited:
                queue.append((nr, nc, moves + 1))
                visited.add((nr, nc))

    return f'Kate got out in {max_moves + 1} moves' if max_moves != -1 else 'Kate cannot get out'


if __name__ == '__main__':
    maze = read_maze()
    print(get_longest_escape(maze))

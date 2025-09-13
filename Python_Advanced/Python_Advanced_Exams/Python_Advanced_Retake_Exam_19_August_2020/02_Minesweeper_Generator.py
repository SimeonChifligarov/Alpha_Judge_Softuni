n = int(input())
bombs_count = int(input())

field = [[0] * n for _ in range(n)]
bombs = []

for _ in range(bombs_count):
    r, c = input().strip()[1:-1].split(", ")
    bombs.append((int(r), int(c)))
for r, c in bombs:
    field[r][c] = "*"
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for r, c in bombs:
    for dr, dc in directions:
        rr, cc = r + dr, c + dc
        if 0 <= rr < n and 0 <= cc < n and field[rr][cc] != "*":
            field[rr][cc] += 1
for row in field:
    print(" ".join(str(x) for x in row))

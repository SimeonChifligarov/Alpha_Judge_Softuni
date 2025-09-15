n = int(input())
matrix = [list(input()) for _ in range(n)]

snake = None
burrows = []
for r in range(n):
    for c in range(n):
        if matrix[r][c] == "S":
            snake = [r, c]
        elif matrix[r][c] == "B":
            burrows.append((r, c))
food = 0
moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
won = False
while True:
    cmd = input()
    matrix[snake[0]][snake[1]] = "."
    dr, dc = moves[cmd]
    nr, nc = snake[0] + dr, snake[1] + dc
    if not (0 <= nr < n and 0 <= nc < n):
        break
    if matrix[nr][nc] == "*":
        food += 1
        matrix[nr][nc] = "S"
        snake = [nr, nc]
        if food == 10:
            won = True
            break
    elif matrix[nr][nc] == "B":
        matrix[nr][nc] = "."
        if burrows:
            a, b = burrows
            tr, tc = b if (nr, nc) == a else a
            matrix[tr][tc] = "S"
            snake = [tr, tc]
            matrix[a[0]][a[1]] = "."
            matrix[b[0]][b[1]] = "."
    else:
        matrix[nr][nc] = "S"
        snake = [nr, nc]
print("You won! You fed the snake." if won else "Game over!")
print(f"Food eaten: {food}")
for row in matrix:
    print("".join(row))

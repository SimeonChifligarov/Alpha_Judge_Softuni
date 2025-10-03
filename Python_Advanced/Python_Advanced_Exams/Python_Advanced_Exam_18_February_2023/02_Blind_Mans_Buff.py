n, m = map(int, input().split())
grid = [input().split() for _ in range(n)]

r = c = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == "B":
            r, c = i, j
            grid[i][j] = "-"
            break

moves_map = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
touched = 0
moves = 0

while True:
    cmd = input()
    if cmd == "Finish" or touched == 3:
        break
    dr, dc = moves_map[cmd]
    nr, nc = r + dr, c + dc
    if not (0 <= nr < n and 0 <= nc < m):
        continue
    if grid[nr][nc] == "O":
        continue
    if grid[nr][nc] == "P":
        touched += 1
        moves += 1
        grid[nr][nc] = "-"
        r, c = nr, nc
    else:
        moves += 1
        r, c = nr, nc

print("Game over!")
print(f"Touched opponents: {touched} Moves made: {moves}")

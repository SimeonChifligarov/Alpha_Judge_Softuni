n, m = map(int, input().split(","))
grid = [list(input()) for _ in range(n)]
moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

r = c = 0
cheese = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == "M":
            r, c = i, j
        if grid[i][j] == "C":
            cheese += 1

while True:
    cmd = input()
    if cmd == "danger":
        print("Mouse will come back later!")
        grid[r][c] = "M"
        for row in grid:
            print("".join(row))
        break
    dr, dc = moves[cmd]
    nr, nc = r + dr, c + dc
    if not (0 <= nr < n and 0 <= nc < m):
        print("No more cheese for tonight!")
        grid[r][c] = "M"
        for row in grid:
            print("".join(row))
        break
    if grid[nr][nc] == "@":
        continue
    grid[r][c] = "*"
    r, c = nr, nc
    if grid[r][c] == "C":
        cheese -= 1
        if cheese == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            grid[r][c] = "M"
            for row in grid:
                print("".join(row))
            break
        grid[r][c] = "M"
    elif grid[r][c] == "T":
        print("Mouse is trapped!")
        grid[r][c] = "M"
        for row in grid:
            print("".join(row))
        break
    else:
        grid[r][c] = "M"

dims = input().split(", ")
rows, cols = int(dims[0]), int(dims[1])

grid = [list(input().strip()) for _ in range(rows)]

sr = sc = br = bc = -1
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 'C':
            sr, sc = i, j
        elif grid[i][j] == 'B':
            br, bc = i, j

r, c = sr, sc
t = 16
won = False
killed = False
exploded = False
defuse_fail = False
needed = 0

moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while True:
    cmd = input()
    if won or killed or exploded or defuse_fail:
        break
    if cmd in moves:
        if t <= 0:
            exploded = True
            break
        dr, dc = moves[cmd]
        nr, nc = r + dr, c + dc
        t -= 1
        if 0 <= nr < rows and 0 <= nc < cols:
            r, c = nr, nc
            if grid[r][c] == 'T':
                grid[r][c] = '*'
                killed = True
                break
        if t == 0 and not killed:
            exploded = True
            break
    elif cmd == 'defuse':
        if r == br and c == bc:
            if t >= 4:
                t -= 4
                grid[br][bc] = 'D'
                won = True
                break
            else:
                needed = 4 - t
                t = 0
                grid[br][bc] = 'X'
                defuse_fail = True
                break
        else:
            t -= 2
            if t <= 0:
                exploded = True
                break

if won:
    print("Counter-terrorist wins!")
    print(f"Bomb has been defused: {t} second/s remaining.")
elif killed:
    print("Terrorists win!")
elif exploded or defuse_fail:
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    print(f"Time needed: {needed} second/s.")

grid[sr][sc] = 'C'
for row in grid:
    print("".join(row))

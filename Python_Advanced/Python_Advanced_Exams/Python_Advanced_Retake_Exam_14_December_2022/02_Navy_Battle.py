n = int(input())
grid = [list(input()) for _ in range(n)]

r = c = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == "S":
            r, c = i, j
            grid[i][j] = "-"
cruisers = sum(row.count("C") for row in grid)
hits = 0
moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    cmd = input()
    dr, dc = moves[cmd]
    r, c = r + dr, c + dc
    if grid[r][c] == "*":
        hits += 1
        grid[r][c] = "-"
        if hits == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{r}, {c}]!")
            grid[r][c] = "S"
            for row in grid:
                print("".join(row))
            break
    elif grid[r][c] == "C":
        cruisers -= 1
        grid[r][c] = "-"
        if cruisers == 0:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            grid[r][c] = "S"
            for row in grid:
                print("".join(row))
            break

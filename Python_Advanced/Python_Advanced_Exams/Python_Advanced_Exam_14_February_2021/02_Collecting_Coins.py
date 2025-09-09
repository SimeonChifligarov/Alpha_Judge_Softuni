n = int(input())
grid = [input().split() for _ in range(n)]

r = c = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == "P":
            r, c = i, j

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
coins = 0
path = [[r, c]]
won = False

while True:
    cmd = input()
    if cmd not in moves:
        continue
    dr, dc = moves[cmd]
    r = (r + dr) % n
    c = (c + dc) % n
    path.append([r, c])
    if grid[r][c] == "X":
        coins //= 2
        print(f"Game over! You've collected {coins} coins.")
        break
    if grid[r][c].isdigit():
        coins += int(grid[r][c])
        grid[r][c] = "0"
        if coins >= 100:
            print(f"You won! You've collected {coins} coins.")
            won = True
            break

print("Your path:")
for p in path:
    print(f"[{p[0]}, {p[1]}]")

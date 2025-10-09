n = int(input())
grid = [input().split() for _ in range(n)]

pr = pc = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'P':
            pr, pc = i, j

stars = 2
won = False
lost = False
first_move_done = False

dirs = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while True:
    cmd = input()
    if won or lost:
        break
    if not first_move_done:
        grid[pr][pc] = '.'
        first_move_done = True
    dr, dc = dirs[cmd]
    nr, nc = pr + dr, pc + dc
    if not (0 <= nr < n and 0 <= nc < n):
        pr, pc = 0, 0
    else:
        if grid[nr][nc] == '#':
            stars -= 1
            if stars <= 0:
                lost = True
                break
            continue
        pr, pc = nr, nc
    if grid[pr][pc] == '*':
        stars += 1
        grid[pr][pc] = '.'
        if stars >= 10:
            won = True
            break

if won:
    print("You won! You have collected 10 stars.")
else:
    print("Game over! You are out of any stars.")
print(f"Your final position is [{pr}, {pc}]")
grid[pr][pc] = 'P'
for row in grid:
    print(" ".join(row))

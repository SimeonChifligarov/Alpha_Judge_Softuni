n = int(input())
grid = [input().split() for _ in range(n)]

sx = sy = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            sx, sy = i, j

x, y = sx, sy
resources = 100
grid[x][y] = '.'
reached = False
failed_lost = False
failed_stranded = False

dirs = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while True:
    cmd = input()

    dx, dy = dirs[cmd]
    nx, ny = x + dx, y + dy
    if not (0 <= nx < n and 0 <= ny < n):
        failed_lost = True
        break
    x, y = nx, ny
    resources -= 5
    if grid[x][y] == 'R':
        resources = min(100, resources + 10)
    elif grid[x][y] == 'M':
        resources -= 5
        grid[x][y] = '.'
    if grid[x][y] == 'P':
        reached = True
        break
    if resources < 5:
        failed_stranded = True
        break

if reached:
    print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
elif failed_lost:
    print("Mission failed! The spaceship was lost in space.")
    grid[x][y] = 'S'
elif failed_stranded:
    print("Mission failed! The spaceship was stranded in space.")
    grid[x][y] = 'S'
else:
    print("Mission failed! The spaceship was stranded in space.")
    grid[x][y] = 'S'

for row in grid:
    print(" ".join(row))

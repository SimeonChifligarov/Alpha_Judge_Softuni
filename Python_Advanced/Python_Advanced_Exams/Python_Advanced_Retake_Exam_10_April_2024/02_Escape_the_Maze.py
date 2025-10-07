n = int(input().strip())
field = [list(input().strip()) for _ in range(n)]

r = c = 0
for i in range(n):
    for j in range(n):
        if field[i][j] == 'P':
            r, c = i, j
            break

health = 100
escaped = False

dirs = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while True:
    cmd = input()

    dr, dc = dirs[cmd]
    nr, nc = r + dr, c + dc
    if not (0 <= nr < n and 0 <= nc < n):
        continue
    field[r][c] = '-'
    cell = field[nr][nc]
    r, c = nr, nc
    if cell == 'M':
        health -= 40
        if health <= 0:
            health = 0
            break
        field[r][c] = '-'
    elif cell == 'H':
        health = min(100, health + 15)
        field[r][c] = '-'
    elif cell == 'X':
        escaped = True
        break

field[r][c] = 'P'

if health <= 0:
    print("Player is dead. Maze over!")
elif escaped:
    print("Player escaped the maze. Danger passed!")
print(f"Player's health: {health} units")
for row in field:
    print(''.join(row))

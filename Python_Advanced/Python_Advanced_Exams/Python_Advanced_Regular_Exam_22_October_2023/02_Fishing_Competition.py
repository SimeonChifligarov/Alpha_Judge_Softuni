n = int(input().strip())
area = [list(input().strip()) for _ in range(n)]

r = c = 0
for i in range(n):
    for j in range(n):
        if area[i][j] == 'S':
            r, c = i, j
            break

caught = 0
dirs = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

lost = False
while True:
    cmd = input()
    if cmd == 'collect the nets':
        break
    dr, dc = dirs[cmd]
    area[r][c] = '-'
    r = (r + dr) % n
    c = (c + dc) % n
    cell = area[r][c]
    if cell == 'W':
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{r},{c}]")
        lost = True
        break
    if cell.isdigit():
        caught += int(cell)
    area[r][c] = 'S'

if not lost:
    if caught >= 20:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - caught} tons of fish more.")
    if caught > 0:
        print(f"Amount of fish caught: {caught} tons.")
    for row in area:
        print(''.join(row))

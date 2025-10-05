n = int(input().strip())
air = [list(input().strip()) for _ in range(n)]

r = c = 0
enemies = 0
for i in range(n):
    for j in range(n):
        if air[i][j] == 'J':
            r, c = i, j
        elif air[i][j] == 'E':
            enemies += 1

armor = 300
dirs = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
message = ""

while True:
    cmd = input()
    dr, dc = dirs[cmd]
    air[r][c] = '-'
    r += dr
    c += dc
    cell = air[r][c]
    if cell == 'E':
        enemies -= 1
        air[r][c] = '-'
        if enemies == 0:
            message = "Mission accomplished, you neutralized the aerial threat!"
            break
        armor -= 100
        if armor == 0:
            message = f"Mission failed, your jetfighter was shot down! Last coordinates [{r}, {c}]!"
            break
    elif cell == 'R':
        armor = 300
        air[r][c] = '-'
    if enemies == 0:
        message = "Mission accomplished, you neutralized the aerial threat!"
        break

air[r][c] = 'J'
print(message)
for row in air:
    print(''.join(row))

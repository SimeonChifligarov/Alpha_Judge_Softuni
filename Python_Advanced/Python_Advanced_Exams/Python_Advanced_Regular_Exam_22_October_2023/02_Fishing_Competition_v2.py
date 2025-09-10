QUOTA = 20
DIRS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

n = int(input().strip())
area = [list(input().strip()) for _ in range(n)]

r = c = 0
found = False
for i in range(n):
    for j in range(n):
        if area[i][j] == 'S':
            r, c = i, j
            found = True
            break
    if found:
        break

caught = 0
lost = False

while True:
    cmd = input().strip()
    if cmd == 'collect the nets':
        break

    dr, dc = DIRS[cmd]

    area[r][c] = '-'

    r = (r + dr) % n
    c = (c + dc) % n

    cell = area[r][c]
    if cell == 'W':
        print(
            f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
            f"Last coordinates of the ship: [{r},{c}]"
        )
        lost = True
        break

    if cell.isdigit():
        caught += int(cell)

    area[r][c] = 'S'

if not lost:
    if caught >= QUOTA:
        print("Success! You managed to reach the quota!")
    else:
        print(
            "You didn't catch enough fish and didn't reach the quota! "
            f"You need {QUOTA - caught} tons of fish more."
        )
    if caught > 0:
        print(f"Amount of fish caught: {caught} tons.")
    for row in area:
        print(''.join(row))

n = int(input().strip())
field = [list(input().strip()) for _ in range(n)]

row = col = 0
for r in range(n):
    for c in range(n):
        if field[r][c] == 'B':
            row, col = r, c
            break

moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
energy = 15
nectar = 0
restored = False
hive_reached = False
ran_out = False

while True:
    cmd = input()
    field[row][col] = '-'
    dr, dc = moves[cmd]
    row = (row + dr) % n
    col = (col + dc) % n
    energy -= 1
    cell = field[row][col]
    if cell.isdigit():
        nectar += int(cell)
        field[row][col] = '-'
    if cell == 'H':
        hive_reached = True
        break
    if energy == 0:
        if not restored and nectar >= 30:
            energy += nectar - 30
            nectar = 30
            restored = True
            if energy == 0:
                ran_out = True
                break
        else:
            ran_out = True
            break

field[row][col] = 'B'

if hive_reached:
    if nectar >= 30:
        print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
    else:
        print("Beesy did not manage to collect enough nectar.")
elif ran_out:
    print("This is the end! Beesy ran out of energy.")

for r in field:
    print(''.join(r))

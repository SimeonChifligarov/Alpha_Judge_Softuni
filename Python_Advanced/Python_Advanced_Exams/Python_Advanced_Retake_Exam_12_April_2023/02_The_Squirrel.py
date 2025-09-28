n = int(input())
commands = input().split(", ")
field = [list(input()) for _ in range(n)]

r = c = 0
for i in range(n):
    for j in range(n):
        if field[i][j] == "s":
            r, c = i, j

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
hazelnuts = 0
ended = False

for cmd in commands:
    dr, dc = moves[cmd]
    nr, nc = r + dr, c + dc
    if not (0 <= nr < n and 0 <= nc < n):
        print("The squirrel is out of the field.")
        ended = True
        break
    r, c = nr, nc
    if field[r][c] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        ended = True
        break
    if field[r][c] == "h":
        hazelnuts += 1
        field[r][c] = "*"
        if hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            ended = True
            break

if not ended:
    if hazelnuts < 3:
        print("There are more hazelnuts to collect.")
    else:
        print("Good job! You have collected all hazelnuts!")

print(f"Hazelnuts collected: {hazelnuts}")

rows, cols = map(int, input().split(", "))
grid = [input().split() for _ in range(rows)]

r = c = 0
total_items = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "Y":
            r, c = i, j
        if grid[i][j] in {"D", "G", "C"}:
            total_items += 1

collected = {"D": 0, "G": 0, "C": 0}
moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
finished = False

while not finished:
    # try:
    #     line = input()
    # except EOFError:
    #     break
    line = input()
    if line == "End":
        break
    direction, steps = line.split("-")
    steps = int(steps)
    for _ in range(steps):
        grid[r][c] = "x"
        dr, dc = moves[direction]
        r = (r + dr) % rows
        c = (c + dc) % cols
        if grid[r][c] in collected:
            collected[grid[r][c]] += 1
            total_items -= 1
        if total_items == 0:
            finished = True
            break
        grid[r][c] = "x"

grid[r][c] = "Y"

if total_items == 0:
    print("Merry Christmas!")
print("You've collected:")
print(f"- {collected['D']} Christmas decorations")
print(f"- {collected['G']} Gifts")
print(f"- {collected['C']} Cookies")
for row in grid:
    print(" ".join(row))

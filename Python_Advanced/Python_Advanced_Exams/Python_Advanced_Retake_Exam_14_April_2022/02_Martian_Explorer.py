grid = [input().split() for _ in range(6)]
commands = input().split(", ")

r = c = 0
for i in range(6):
    for j in range(6):
        if grid[i][j] == "E":
            r, c = i, j
            break

found = {"W": 0, "M": 0, "C": 0}
names = {"W": "Water", "M": "Metal", "C": "Concrete"}
moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
broken = False

for cmd in commands:
    dr, dc = moves[cmd]
    r = (r + dr) % 6
    c = (c + dc) % 6
    cell = grid[r][c]
    if cell in "WMC":
        found[cell] += 1
        print(f"{names[cell]} deposit found at ({r}, {c})")
    elif cell == "R":
        print(f"Rover got broken at ({r}, {c})")
        broken = True
        break

if all(found[x] > 0 for x in "WMC"):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

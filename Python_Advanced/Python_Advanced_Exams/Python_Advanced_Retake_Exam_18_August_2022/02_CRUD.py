matrix = [input().split() for _ in range(6)]
# r, c = eval(input())
r, c = map(int, input().strip("()").split(", "))
dirs = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    line = input()
    if line == "Stop":
        break
    parts = line.split(", ")
    cmd, direction = parts[0], parts[1]
    dr, dc = dirs[direction]
    r, c = r + dr, c + dc
    if cmd == "Create":
        value = parts[2]
        if matrix[r][c] == ".":
            matrix[r][c] = value
    elif cmd == "Update":
        value = parts[2]
        if matrix[r][c] != ".":
            matrix[r][c] = value
    elif cmd == "Delete":
        if matrix[r][c] != ".":
            matrix[r][c] = "."
    elif cmd == "Read":
        if matrix[r][c] != ".":
            print(matrix[r][c])

for row in matrix:
    print(" ".join(row))

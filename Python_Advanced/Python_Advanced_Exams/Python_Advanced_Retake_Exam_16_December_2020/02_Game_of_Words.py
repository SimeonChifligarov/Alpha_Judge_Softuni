s = input()
n = int(input())
field = [list(input()) for _ in range(n)]

pr = pc = 0
for i in range(n):
    if "P" in field[i]:
        pr, pc = i, field[i].index("P")
        break

m = int(input())
moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

for _ in range(m):
    cmd = input()
    dr, dc = moves[cmd]
    nr, nc = pr + dr, pc + dc
    if not (0 <= nr < n and 0 <= nc < n):
        if s:
            s = s[:-1]
        continue
    field[pr][pc] = "-"
    if field[nr][nc].isalpha():
        s += field[nr][nc]
    pr, pc = nr, nc
    field[pr][pc] = "P"

print(s)
for row in field:
    print("".join(row))

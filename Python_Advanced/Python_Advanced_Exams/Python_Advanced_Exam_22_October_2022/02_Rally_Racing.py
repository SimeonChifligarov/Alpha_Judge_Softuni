n = int(input())
car_num = input().strip()
track = [input().split() for _ in range(n)]

tunnels = []
for i in range(n):
    for j in range(n):
        if track[i][j] == "T":
            tunnels.append((i, j))

r = c = 0
km = 0
finished = False
dirs = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    cmd = input().strip()
    if cmd == "End" or finished:
        break
    dr, dc = dirs[cmd]
    r, c = r + dr, c + dc
    if track[r][c] == ".":
        km += 10
    elif track[r][c] == "T":
        km += 30
        tr, tc = r, c
        track[tr][tc] = "."
        other = tunnels[0] if tunnels[1] == (tr, tc) else tunnels[1]
        orr, occ = other
        track[orr][occ] = "."
        r, c = orr, occ
    elif track[r][c] == "F":
        km += 10
        finished = True

if finished:
    print(f"Racing car {car_num} finished the stage!")
else:
    print(f"Racing car {car_num} DNF.")
print(f"Distance covered {km} km.")

track[r][c] = "C"
for row in track:
    print("".join(row))

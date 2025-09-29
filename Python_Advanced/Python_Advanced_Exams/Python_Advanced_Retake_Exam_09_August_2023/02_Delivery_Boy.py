def is_valid(v, limit):
    return 0 <= v < limit


def next_move(cmd, r, c, rows, cols):
    if cmd == "up" and is_valid(r - 1, rows):
        return r - 1, c
    if cmd == "down" and is_valid(r + 1, rows):
        return r + 1, c
    if cmd == "left" and is_valid(c - 1, cols):
        return r, c - 1
    if cmd == "right" and is_valid(c + 1, cols):
        return r, c + 1
    return None, None


rows, cols = map(int, input().split())
field = [list(input()) for _ in range(rows)]

sr = sc = None
r = c = None
for i in range(rows):
    if "B" in field[i]:
        r = i
        c = field[i].index("B")
        sr, sc = r, c
        break

while True:
    cmd = input()
    nr, nc = next_move(cmd, r, c, rows, cols)
    if nr is None or nc is None:
        print("The delivery is late. Order is canceled.")
        field[sr][sc] = " "
        break
    if field[nr][nc] == "*":
        continue
    if field[nr][nc] == "A":
        field[r][c] = "."
        r, c = nr, nc
        field[r][c] = "P"
        print("Pizza is delivered on time! Next order...")
        field[sr][sc] = "B"
        break
    if field[nr][nc] == "P":
        field[r][c] = "."
        r, c = nr, nc
        field[r][c] = "R"
        print("Pizza is collected. 10 minutes for delivery.")
        continue
    if field[r][c] != "R":
        field[r][c] = "."
    r, c = nr, nc
    field[r][c] = "."

for row in field:
    print("".join(row))

board = [input().split() for _ in range(8)]

kr = kc = 0
for r in range(8):
    for c in range(8):
        if board[r][c] == "K":
            kr, kc = r, c
            break

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
attackers = []

for dr, dc in directions:
    r, c = kr + dr, kc + dc
    while 0 <= r < 8 and 0 <= c < 8:
        if board[r][c] == "Q":
            attackers.append([r, c])
            break
        if board[r][c] != ".":
            break
        r += dr
        c += dc

if attackers:
    for pos in attackers:
        print(pos)
else:
    print("The king is safe!")

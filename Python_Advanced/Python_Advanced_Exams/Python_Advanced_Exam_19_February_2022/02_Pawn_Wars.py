board = [input().split() for _ in range(8)]

letters = "abcdefgh"
wr = wc = br = bc = None
for i in range(8):
    for j in range(8):
        if board[i][j] == "w":
            wr, wc = i, j
        elif board[i][j] == "b":
            br, bc = i, j


def square(r, c):
    return f"{letters[c]}{8 - r}"


while True:
    if (wr - 1, wc - 1) == (br, bc) or (wr - 1, wc + 1) == (br, bc):
        print(f"Game over! White win, capture on {square(br, bc)}.")
        break
    wr -= 1
    if wr == 0:
        print(f"Game over! White pawn is promoted to a queen at {square(wr, wc)}.")
        break
    if (br + 1, bc - 1) == (wr, wc) or (br + 1, bc + 1) == (wr, wc):
        print(f"Game over! Black win, capture on {square(wr, wc)}.")
        break
    br += 1
    if br == 7:
        print(f"Game over! Black pawn is promoted to a queen at {square(br, bc)}.")
        break

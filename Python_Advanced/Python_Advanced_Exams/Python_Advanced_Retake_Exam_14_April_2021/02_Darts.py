p1, p2 = input().split(", ")
board = [input().split() for _ in range(7)]

scores = {p1: 501, p2: 501}
throws = {p1: 0, p2: 0}
players = [p1, p2]
turn = 0

while True:
    r, c = map(int, input().strip("()").split(", "))
    player = players[turn % 2]
    throws[player] += 1
    if not (0 <= r < 7 and 0 <= c < 7):
        turn += 1
        continue
    cell = board[r][c]
    if cell == "B":
        print(f"{player} won the game with {throws[player]} throws!")
        break
    if cell == "D" or cell == "T":
        s = int(board[r][0]) + int(board[r][6]) + int(board[0][c]) + int(board[6][c])
        if cell == "D":
            scores[player] -= 2 * s
        else:
            scores[player] -= 3 * s
    else:
        scores[player] -= int(cell)
    if scores[player] <= 0:
        print(f"{player} won the game with {throws[player]} throws!")
        break
    turn += 1

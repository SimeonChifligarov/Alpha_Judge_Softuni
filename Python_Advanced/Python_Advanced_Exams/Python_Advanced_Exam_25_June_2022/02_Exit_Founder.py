players = input().split(", ")
board = [input().split() for _ in range(6)]
rest = {players[0]: False, players[1]: False}
turn = 0

while True:
    r, c = map(int, input().strip("()").split(", "))
    player = players[turn % 2]
    if rest[player]:
        rest[player] = False
        turn += 1
        continue
    cell = board[r][c]
    if cell == "E":
        print(f"{player} found the Exit and wins the game!")
        break
    if cell == "T":
        other = players[(turn + 1) % 2]
        print(f"{player} is out of the game! The winner is {other}.")
        break
    if cell == "W":
        print(f"{player} hits a wall and needs to rest.")
        rest[player] = True
    turn += 1

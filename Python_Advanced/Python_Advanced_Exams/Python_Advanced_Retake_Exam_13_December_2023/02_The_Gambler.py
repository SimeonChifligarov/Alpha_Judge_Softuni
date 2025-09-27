n = int(input())
board = [list(input()) for _ in range(n)]

r = c = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 'G':
            r, c = i, j
            break

amount = 100
dirs = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

won = False
lost = False

while True:
    cmd = input()
    if cmd == 'end':
        break
    dr, dc = dirs[cmd]
    nr, nc = r + dr, c + dc
    board[r][c] = '-'
    if not (0 <= nr < n and 0 <= nc < n):
        print("Game over! You lost everything!")
        lost = True
        break
    cell = board[nr][nc]
    r, c = nr, nc
    if cell == 'W':
        amount += 100
        board[r][c] = '-'
    elif cell == 'P':
        amount -= 200
        board[r][c] = '-'
        if amount <= 0:
            print("Game over! You lost everything!")
            lost = True
            break
    elif cell == 'J':
        amount += 100000
        board[r][c] = 'G'
        print("You win the Jackpot!")
        print(f"End of the game. Total amount: {amount}$")
        for row in board:
            print(''.join(row))
        won = True
        break

if not won and not lost:
    board[r][c] = 'G'
    print(f"End of the game. Total amount: {amount}$")
    for row in board:
        print(''.join(row))

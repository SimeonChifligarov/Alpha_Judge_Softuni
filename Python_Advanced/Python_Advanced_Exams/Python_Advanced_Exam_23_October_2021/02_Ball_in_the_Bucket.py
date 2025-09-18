board = [input().split() for _ in range(6)]
hits = set()
points = 0


def col_sum(c):
    s = 0
    for r in range(6):
        try:
            s += int(board[r][c])
        except ValueError:
            s += 0
    return s


for _ in range(3):
    r, c = map(int, input().strip("()").split(", "))
    if not (0 <= r < 6 and 0 <= c < 6):
        continue
    if board[r][c] == "B" and (r, c) not in hits:
        points += col_sum(c)
        hits.add((r, c))

if 100 <= points <= 199:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif 200 <= points <= 299:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
elif points >= 300:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")
else:
    print(f"Sorry! You need {100 - points} points more to win a prize.")

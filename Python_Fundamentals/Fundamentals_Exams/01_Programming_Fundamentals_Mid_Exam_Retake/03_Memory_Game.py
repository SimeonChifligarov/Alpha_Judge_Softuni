sequence = input().split()
moves = 0
won = False

while True:
    line = input()
    if line == "end":
        break
    i, j = map(int, line.split())
    moves += 1
    invalid = i == j or i < 0 or j < 0 or i >= len(sequence) or j >= len(sequence)
    if invalid:
        token = f"-{moves}a"
        mid = len(sequence) // 2
        sequence.insert(mid, token)
        sequence.insert(mid, token)
        print("Invalid input! Adding additional elements to the board")
        continue
    if sequence[i] == sequence[j]:
        element = sequence[i]
        hi = max(i, j)
        lo = min(i, j)
        del sequence[hi]
        del sequence[lo]
        print(f"Congrats! You have found matching elements - {element}!")
        if not sequence:
            print(f"You have won in {moves} turns!")
            won = True
            break
    else:
        print("Try again!")
if not won:
    print("Sorry you lose :(")
    print(' '.join(sequence))

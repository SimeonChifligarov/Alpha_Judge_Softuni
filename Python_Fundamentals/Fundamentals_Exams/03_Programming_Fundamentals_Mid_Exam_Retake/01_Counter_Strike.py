energy = int(input())

wins = 0
while True:
    line = input()
    if line == "End of battle":
        print(f"Won battles: {wins}. Energy left: {energy}")
        break
    dist = int(line)
    if energy < dist:
        print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
        break
    energy -= dist
    wins += 1
    if wins % 3 == 0:
        energy += wins

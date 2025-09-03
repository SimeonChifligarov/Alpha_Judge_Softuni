targets = list(map(int, input().split()))

while True:
    line = input()
    if line == "End":
        break
    parts = line.split()
    cmd = parts[0]
    if cmd == "Shoot":
        idx = int(parts[1])
        power = int(parts[2])
        if 0 <= idx < len(targets):
            targets[idx] -= power
            if targets[idx] <= 0:
                del targets[idx]
    elif cmd == "Add":
        idx = int(parts[1])
        value = int(parts[2])
        if 0 <= idx < len(targets):
            targets.insert(idx, value)
        else:
            print("Invalid placement!")
    elif cmd == "Strike":
        idx = int(parts[1])
        radius = int(parts[2])
        left = idx - radius
        right = idx + radius
        if left >= 0 and right < len(targets):
            del targets[left:right + 1]
        else:
            print("Strike missed!")

print("|".join(map(str, targets)))

targets = list(map(int, input().split()))

shot = 0
while True:
    line = input()
    if line == "End":
        break
    idx = int(line)
    if 0 <= idx < len(targets) and targets[idx] != -1:
        val = targets[idx]
        targets[idx] = -1
        shot += 1
        for i in range(len(targets)):
            if targets[i] == -1:
                continue
            if targets[i] > val:
                targets[i] -= val
            else:
                targets[i] += val

print(f"Shot targets: {shot} -> {' '.join(map(str, targets))}")

groceries = input().split("!")

while True:
    line = input()
    if line == "Go Shopping!":
        break
    parts = line.split()
    cmd = parts[0]
    if cmd == "Urgent":
        item = parts[1]
        if item not in groceries:
            groceries.insert(0, item)
    elif cmd == "Unnecessary":
        item = parts[1]
        if item in groceries:
            groceries.remove(item)
    elif cmd == "Correct":
        old, new = parts[1], parts[2]
        if old in groceries:
            idx = groceries.index(old)
            groceries[idx] = new
    elif cmd == "Rearrange":
        item = parts[1]
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)

print(", ".join(groceries))

items = input().split(", ")

while True:
    line = input()
    if line == "Craft!":
        break
    line = line.replace(" – ", " - ")
    cmd, arg = line.split(" - ", 1)
    if cmd == "Collect":
        if arg not in items:
            items.append(arg)
    elif cmd == "Drop":
        if arg in items:
            items.remove(arg)
    elif cmd == "Combine Items":
        old, new = arg.split(":")
        if old in items:
            idx = items.index(old) + 1
            items.insert(idx, new)
    elif cmd == "Renew":
        if arg in items:
            items.remove(arg)
            items.append(arg)

print(", ".join(items))

chest = input().split("|")

while True:
    line = input()
    if line == "Yohoho!":
        break
    parts = line.split()
    cmd = parts[0]
    if cmd == "Loot":
        for item in parts[1:]:
            if item not in chest:
                chest.insert(0, item)
    elif cmd == "Drop":
        idx = int(parts[1])
        if 0 <= idx < len(chest):
            chest.append(chest.pop(idx))
    elif cmd == "Steal":
        count = int(parts[1])
        if count >= len(chest):
            stolen = chest[:]
            chest.clear()
        else:
            stolen = chest[-count:]
            chest = chest[:-count]
        print(", ".join(stolen))

avg = sum(len(x) for x in chest) / len(chest) if chest else 0
if chest:
    print(f"Average treasure gain: {avg:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")

n = int(input())

plants = {}
ratings = {}
for _ in range(n):
    name, rarity = input().split("<->")
    plants[name] = int(rarity)
    if name not in ratings:
        ratings[name] = []
while True:
    line = input()
    if line == "Exhibition":
        break
    if line.startswith("Rate: "):
        name, val = line[6:].split(" - ")
        if name in plants:
            ratings.setdefault(name, []).append(float(val))
        else:
            print("error")
    elif line.startswith("Update: "):
        name, val = line[8:].split(" - ")
        if name in plants:
            plants[name] = int(val)
        else:
            print("error")
    elif line.startswith("Reset: "):
        name = line[7:]
        if name in plants:
            ratings[name] = []
        else:
            print("error")

print("Plants for the exhibition:")
for name in plants:
    avg = sum(ratings.get(name, [])) / len(ratings.get(name, [])) if ratings.get(name, []) else 0
    print(f"- {name}; Rarity: {plants[name]}; Rating: {avg:.2f}")

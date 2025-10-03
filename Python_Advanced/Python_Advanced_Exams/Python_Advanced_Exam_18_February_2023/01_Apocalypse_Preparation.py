from collections import deque

textiles = deque(map(int, input().split()))
medicaments = list(map(int, input().split()))

items = {"Patch": 0, "Bandage": 0, "MedKit": 0}
targets = {30: "Patch", 40: "Bandage", 100: "MedKit"}

while textiles and medicaments:
    t = textiles.popleft()
    m = medicaments.pop()
    s = t + m
    if s in targets:
        items[targets[s]] += 1
    elif s > 100:
        items["MedKit"] += 1
        remainder = s - 100
        if medicaments:
            medicaments[-1] += remainder
        else:
            medicaments.append(remainder)
    else:
        medicaments.append(m + 10)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

for name, count in sorted(((k, v) for k, v in items.items() if v > 0), key=lambda x: (-x[1], x[0])):
    print(f"{name} - {count}")

if medicaments:
    print("Medicaments left: " + ", ".join(map(str, reversed(medicaments))))
elif textiles:
    print("Textiles left: " + ", ".join(map(str, textiles)))

from collections import deque

materials = list(map(int, input().split()))
magic = deque(map(int, input().split()))

gifts = {"Gemstone": 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}


def craft(total):
    if 100 <= total <= 199:
        return "Gemstone"
    if 200 <= total <= 299:
        return "Porcelain Sculpture"
    if 300 <= total <= 399:
        return "Gold"
    if 400 <= total <= 499:
        return "Diamond Jewellery"


while materials and magic:
    m = materials[-1]
    k = magic[0]
    total = m + k
    if total < 100:
        if total % 2 == 0:
            total = m * 2 + k * 3
        else:
            total = (m + k) * 2
    elif total > 499:
        total = (m + k) / 2
    item = craft(total) if isinstance(total, (int, float)) else None
    materials.pop()
    magic.popleft()
    if item:
        gifts[item] += 1

success = (gifts["Gemstone"] > 0 and gifts["Porcelain Sculpture"] > 0) or (
            gifts["Gold"] > 0 and gifts["Diamond Jewellery"] > 0)

if success:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print("Materials left: " + ", ".join(map(str, materials)))
if magic:
    print("Magic left: " + ", ".join(map(str, magic)))

for name in sorted(gifts):
    if gifts[name] > 0:
        print(f"{name}: {gifts[name]}")

import re

s = input()

items = []
for m in re.finditer(r'([#|])([A-Za-z ]+)\1(\d{2}/\d{2}/\d{2})\1(\d{1,5})\1', s):
    name, date, cal = m.group(2), m.group(3), int(m.group(4))
    if 0 <= cal <= 10000:
        items.append((name, date, cal))
total = sum(c for _, _, c in items)

print(f"You have food to last you for: {total // 2000} days!")
for name, date, cal in items:
    print(f"Item: {name}, Best before: {date}, Nutrition: {cal}")
